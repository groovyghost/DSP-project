from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "mysql+pymysql://user:user#123@127.0.0.1:3306/userdb"

engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False,bind=engine)
