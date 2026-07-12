from sqlalchemy import select, insert, update, delete
from sqlalchemy.engine import Connection
from database import notes
import schemas

def create_notes(conn: Connection, 
                 note: schemas.NoteCreate, 
                 user_id: int):
    stmt = insert(notes).values(
        title=note.title,
        content=note.content,
        is_public=note.is_public,
        user_id=user_id
    )
    result = conn.execute(stmt)
    conn.commit()
    new_id = result.inserted_primary_key[0]
    return get_note(conn, new_id)

def get_notes(conn: Connection,
              skip: int = 0,
              limit: int = 100):
    stmt = select(notes).offset(skip).limit(limit)
    result = conn.execute(stmt)
    return result.mappings().all()

def get_note(conn: Connection, 
             note_id: int):
    stmt = select(notes).where(notes.c.id == note_id)
    result = conn.execute(stmt)
    return result.mappings().first()

def update_note(conn: Connection,
                note: schemas.NoteUpdate,
                note_id: int):
    update_data = note.model_dump(exclude_unset=True)
    if not update_data:
        return get_note(get_note(conn, note_id))
    stmt = update(notes).where(notes.c.id == note_id).values(**update_data)
    conn.execute(stmt)
    conn.commit()
    return get_note(conn, note_id)

def delete_note(conn: Connection,
                note_id: int):
    existing = get_note(conn, note_id)
    if not existing:
        return None
    stmt = delete(notes).where(notes.c.id == note_id)
    conn.execute(stmt)
    conn.commit()
    return existing