# HTTPie

https://httpie.io

User-friendly HTTP client for API testing. Makes headers, JSON bodies, and auth one-liners easy — good for replaying authenticated requests with modified claims/params.

```bash
http POST http://target.com/api/login username=admin password=admin
http GET http://target.com/api/profile "Authorization: Bearer $JWT" role=admin
http --form POST http://target.com/upload file@payload.png
```

- Bare `key=value` pairs become a JSON body for POST/PUT by default.
- `"Header: value"` syntax sets headers inline.
