from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.engine import Connection
from typing import List

import schemas, crud
from database import engine, meta

meta.create_all(engine)

app = FastAPI(title="Notes API")

def get_conn():
    with engine.connect() as conn:
        yield conn

@app.post("/notes/", response_model=schemas.NoteOut)
async def create_note(note: schemas.NoteCreate, 
                      user_id: int,
                      conn: Connection = Depends(get_conn)):
    return crud.create_note(conn, note, user_id)