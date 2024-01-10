from sqlalchemy.orm import Session

from ..utilities import schemas

from ..models import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, name=user.name  # hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.owner_id == id).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_user(db: Session, name: str, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    # user.is_active = is_active
    user.name = name
    db.commit()
    return user


def delete_user(db: Session, id: int):
    user = db.query(models.User).filter(models.User.id == id).first()
    db.delete(user)
    db.commit()
    return user


def upadte_item(db: Session, id: int, description: str):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    item.description = description
    db.commit()
    return item


def delete_item(db: Session, id: int):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    db.delete(item)
    db.commit()
    return item