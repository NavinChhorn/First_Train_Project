from sqlalchemy import Column, Integer, String

from db import Base

from .base_model import BaseModel

class UserModel(BaseModel, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False,index=True)
    username = Column(String(32), nullable=False, index=True)
    password = Column(String(256))

    def __init__(self, schema={}):
        super().__init__()
        for key, value in schema.items():
            if hasattr(self, key):
                setattr(self, key, value)
