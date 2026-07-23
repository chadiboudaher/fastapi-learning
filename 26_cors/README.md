# CORS

CORS is a security mechanism that controls which websites can access your backend api from a browser.

## How it works

1. Browser sends an OPTIONS preflight request to check if the backend allows cross-origin requests.
2. Backend must response with CORS headers that specify which origins are permitted.
3. Only then does the browser allow the actual request.
