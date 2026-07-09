# Handling Errors

FastAPI's `HTTPException` vs Starlette's `HTTPException`?

FastAPI has its own HTTPException. and it is an error class inherited from starlette's HTTPException error class.

The only difference is that FastAPI's HTTPException accepts any JSON-able data for the detail field, while Starlette's HTTPException only accepts strings for it.
