from sqlalchemy import Column, Integer, String

from database import Base


class EmployeerModel(Base):
    __tablename__ = 'employeer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    job = Column(String(255), nullable=True)
