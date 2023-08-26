import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship

from database import Base


class StatusEnum(enum.Enum):
    todo = 'todo'
    doing = 'doing'
    done = 'done'


class TasksModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.todo)
    employee_id = Column(Integer, ForeignKey('employeer.id'))
    parent_id = Column(Integer, ForeignKey('tasks.id'))
    deadline = Column(DateTime(timezone=True), nullable=True)

    employee = relationship("EmployeesModel", backref="tasks")
    parent = relationship("TasksModel", remote_side=id, backref="children")
