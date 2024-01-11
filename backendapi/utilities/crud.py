from sqlalchemy.orm import Session

from ..schemas import schemas

from ..models import models


"""
Get the user based on his user_id
"""
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


"""
Get the  user based on his email
"""
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


"""
Create a user entry and commit to the User table
"""
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email, name=user.name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


"""
Get the items bought by a particular user
"""
def get_items(db: Session, id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.owner_id == id).offset(skip).limit(limit).all()


"""
Create an item entry and commit to the Item table
"""
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


"""
Update the name of the user
"""
def update_user(db: Session, name: str, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    user.name = name
    db.commit()
    return user


"""
Delete the user entry
"""
def delete_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    db.delete(user)
    db.commit()
    return user


"""
Update an item description
"""
def upadte_item(db: Session, id: int, description: str):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    item.description = description
    db.commit()
    return item


"""
Delete an item entry
"""
def delete_item(db: Session, id: int):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    db.delete(item)
    db.commit()
    return item
