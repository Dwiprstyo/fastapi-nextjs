from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from api.core.config import get_db
from api.models.credential import Credential

app = FastAPI()


@app.get("/api/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/credential")
def get_all_cred(db: Session = Depends(get_db)):
    return db.query(Credential).all()