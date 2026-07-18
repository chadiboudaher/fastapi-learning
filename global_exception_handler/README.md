# What is an Exception?

An **exception** is when `something went wrong`

## 1. The basic structure

User Request -> API -> Something goes wrong -> Exception Handler -> Nice Error Response

## 2. There are Different types of Errors

- User send wrong data - `RequestValidationError` is used in this case.
- user ask for something that does not exist.
- when databse is down
