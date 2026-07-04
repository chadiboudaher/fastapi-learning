# Request Body

This is very important.

When we need to send data from a client to your API, your send it as a request body.

`pydantic` provide `BaseModel`, a python class used for creating data schemas.

We used `POST` and `PUT` for the first time.

`model_dump` is used to create a copy of request body.
