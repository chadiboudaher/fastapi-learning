# We create an engine, which we use to connect to a database.
from sqlalchemy import create_engine

engine = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()
