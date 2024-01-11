from pydantic import BaseModel

"""
pydantic schema used for getting the minimum data input from the user Item entry Creation
"""
class ItemBase(BaseModel):
    title: str
    description: str | None = None


"""
pydantic schema used when Item creation
"""
class ItemCreate(ItemBase):
    pass


"""
pydantic schema used to define the whole Item table entry
"""
class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


"""
pydantic schema used for getting the minimum data input from the user for User entry Creation
"""
class UserBase(BaseModel):
    email: str
    name: str


"""
pydantic schema used when User creation
"""
class UserCreate(UserBase):
    # password: str
    pass


"""
pydantic schema used to define the whole User table entry
"""
class User(UserBase):
    id: int
    # is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
