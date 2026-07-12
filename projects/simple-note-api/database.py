

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime 

engine = create_engine("sqlite:///mydatabase.db", 
                       echo=True,
                       connect_args={"check_same_thread": False})

meta = MetaData()

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, index=True, nullable=False),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("full_name", String),
    Column("hashed_password", String, nullable=False),
    Column("disabled", Boolean, default=False),
    Column("created_at", DateTime, default=datetime.utcnow)
)

notes = Table(
    "notes",
    meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
    Column("is_public", Boolean, default=False),
    Column("created_at", DateTime, default=datetime.utcnow),
    Column("updated_at", DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
    Column("user_id", Integer, ForeignKey("users.id"))
)

meta.create_all(engine)

# conn = engine.connect()