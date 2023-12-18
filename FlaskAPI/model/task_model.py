from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from db import Base, engine

from .base_model import BaseModel

class TaskModel(BaseModel, Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    img = Column(String(255), nullable=True)
    description = Column(String(64), nullable=False)
    label = Column(String(20))
    status = Column(Boolean)

    def __init__(self, schema={}):
        super().__init__()
        for key, value in schema.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def get_ordered_tasks(cls):
        session = sessionmaker(bind=engine)()
        ordered_tasks = session.query(cls).order_by(cls.id.asc()).all()
        session.close()
        return ordered_tasks