from pydantic import BaseModel, ConfigDict


class EmployeeStructures(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    job: str
