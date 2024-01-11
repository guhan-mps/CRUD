from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import os
from ..config.database import Base


"""
User table RDBMS schema creation
"""
class User(Base):
    __tablename__ = os.environ['UserModelName']

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    items = relationship("Item", back_populates="owner")


"""
Items table RDBMS schema creation
"""
class Item(Base):
    __tablename__ = os.environ['ItemModelName']

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
