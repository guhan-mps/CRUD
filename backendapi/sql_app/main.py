from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from ..models import models

from ..utilities import schemas

from . import crud
from ..config.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/users/{user_id}/items/", response_model=list[schemas.Item])
def read_items(id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, id=id, skip=skip, limit=limit)
    return items


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(id: int, name: str, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, name, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found!!!")
    return user


@app.put("/users/{user_id}/items", response_model=schemas.Item)
def upadte_item(id: int, description: str, db: Session = Depends(get_db)):
    item = crud.upadte_item(db, id, description)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found!!!")
    return item


@app.delete("/users/{user_id}/items", response_model=schemas.Item)
def delete_item(id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found!!!")
    return item
