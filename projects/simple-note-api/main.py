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

@app.get("/notes/", response_model=List[schemas.NoteOut])
async def read_notes(skip: int = 0, 
                    limit: int = 100, 
                    conn: Connection = Depends(get_conn)):
    return crud.get_notes(conn, skip, limit)

@app.get("/notes/{note_id}", response_model=schemas.NoteOut)
async def read_note(note_id: int,
                    conn: Connection = Depends(get_conn)):
    db_note = crud.get_note(conn, note_id)
    if db_note is None:
        raise HTTPException(status_code=404,
                            detail="Note not found")
    return db_note