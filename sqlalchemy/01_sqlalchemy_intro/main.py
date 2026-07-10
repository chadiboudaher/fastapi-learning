# We create an engine, which we use to connect to a database.
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()


conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))

# To persist the changes
conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)
session.execute(text('INSERT INTO PEOPLE (name, age) VALUES ("Mike", 30)'))
session.commit()