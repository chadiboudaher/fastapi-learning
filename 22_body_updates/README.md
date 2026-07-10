# Body Updates

- Apply partial updates instead of put
- Retrieve the stored data.
- Put the data in a pydantic model
- Generate a `dict` without default values from the input model (using `exclude_unset`).
- Creating a copy of the stored model, updating its attributes with the received partial updates.
- Convert the copied model to something that can be stored in your DB.
