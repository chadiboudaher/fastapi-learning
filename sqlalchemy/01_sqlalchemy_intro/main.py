"""
**engine** act as a source of connections to a particular database.

sqlite+pysqlite:///:memory:
this tell us three things:
1. what kind of data are we communicating with.
2. DBAPI - a third party driver used to interact with a particular databases (pysqlite for SQLite).
3. memory -> meaning we are using in-memory-only database.
"""

from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all()python)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()