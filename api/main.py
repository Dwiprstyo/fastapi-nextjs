from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from api.core.config import get_db
from api.models.users import Users

app = FastAPI()

@app.get("/api/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/user/{user_id}")
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/api/user")
def get_all_cred(db: Session = Depends(get_db)):
    return db.query(Users).all()