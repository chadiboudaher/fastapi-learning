# What is an Exception?

An **exception** is when `something went wrong`

## 1. The basic structure

User Request -> API -> Something goes wrong -> Exception Handler -> Nice Error Response

## 2. There are Different types of Errors

- User send wrong data - `RequestValidationError` is used in this case.
- user ask for something that does not exist.
- when databse is down

## 3. Create Custom Error message

In the error message we can add:

- **success** - True or `False`.
- **timestamp** - `datetime.now()`.
- **path** - `request.url.path`
- _error_:
  - **message** -` str(exc)`.
  - **type** - `type(exc).__name__`
