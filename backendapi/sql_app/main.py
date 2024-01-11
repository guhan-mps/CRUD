from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from ..models import models

from ..schemas import schemas

from ..utilities import crud
from ..config.database import SessionLocal, engine


"""
Create all the tables defined in the models.py
"""
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


"""
Create a database Session to acess the database
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
Create an user entry, if email is already present raises 400 exception
"""
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


"""
Display the user entry of a given user_id, if not found it raises 404 exception
"""
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


"""
Create an item entry for a particular user
"""
@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


"""
Display the  items bought by a particular user
"""
@app.get("/users/{user_id}/items/", response_model=list[schemas.Item])
def read_items(id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, id=id, skip=skip, limit=limit)
    return items


"""
Update the name of the user, if the user is not present it raises 404 exception
"""
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(id: int, name: str, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, name, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


"""
Delete an user entry, if the user is not present it raises 404 exception
"""
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found!!!")
    return user


"""
Update the description of an item, if the item_id is not present it raises 404 exception
"""
@app.put("/users/{user_id}/items", response_model=schemas.Item)
def upadte_item(id: int, description: str, db: Session = Depends(get_db)):
    item = crud.upadte_item(db, id, description)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found!!!")
    return item


"""
Delete an item entry, If the item is not present it raises 404 exception
"""
@app.delete("/users/{user_id}/items", response_model=schemas.Item)
def delete_item(id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found!!!")
    return item
