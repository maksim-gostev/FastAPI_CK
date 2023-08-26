from datetime import datetime

from pydantic import BaseModel

from task.models import StatusEnum
from employeer.structures import EmployeeStructures


class TaskStructures(BaseModel):
    id: int
    name: str
    description: str
    status: StatusEnum
    employee_id: int
    parent_id: int
    deadline: datetime


class TaskCreateStructures(BaseModel):
    name: str
    description: str
    status: StatusEnum
    employee_id: int
    parent_id: int
    deadline: datetime


class TaskImportantStructures(BaseModel):
    task: TaskStructures
    deadline: datetime
    employees: list[EmployeeStructures]
