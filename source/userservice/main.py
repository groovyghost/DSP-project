from typing import List
import logging


import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, SessionLocal, engine
from models import Users

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserSchema(BaseModel):
    name: str
    email: str


class UserCreateSchema(UserSchema):
    password: str


@app.get("/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    return db.query(Users).all()


@app.post("/create_users", response_model=UserSchema)
def create_users(user: UserCreateSchema, db: Session = Depends(get_db)):
    add_user = Users(name=user.name, email=user.email, password=user.password)
    db.add(add_user)
    db.commit()
    return add_user


@app.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == user_id).first()
        u.name = user.name
        u.email = user.email
        db.add(u)
        db.commit()
        return u
    except Exception as error:
        logger.error(f"Caught a generic exception: {error}")

        return HTTPException(status_code=404, detail="user not found")


@app.delete("/users/{user_id}", response_class=JSONResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id == user_id).first()
        db.delete(u)
        db.commit()
        return u
    except Exception as error:
        logger.error(f"Caught a generic exception: {error}")
        return HTTPException(status_code=404, detail="user not found")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=5000, log_level="debug")
