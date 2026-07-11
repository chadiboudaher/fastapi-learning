from fastapi import FastAPI

app = FastAPI(title="Notes api")

@app.get("/")
async def root():
    return {"message": "Hello"}