from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from employeer import service
from employeer.structures import EmployeeStructures

employee_router = APIRouter(prefix="/employeer", tags=["employeer"])


@employee_router.get("/", response_model=list[EmployeeStructures],
                     status_code=status.HTTP_200_OK)
async def get_all_employees(session: AsyncSession = Depends(get_async_session)):
    return await service.get_all_employees(session)


@employee_router.get("/{employee_id}", response_model=EmployeeStructures,
                     status_code=status.HTTP_200_OK)
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    return await service.get_employee_by_id(session, employee_id)


@employee_router.post("/", response_model=EmployeeStructures,
                      status_code=status.HTTP_201_CREATED)
async def create_employee(employee: EmployeeStructures,
                          session: AsyncSession = Depends(get_async_session)):
    return await service.create_employee(session, employee)


@employee_router.put("/{employee_id}", response_model=EmployeeStructures)
async def update_employee(employee_id: int, data: EmployeeStructures,
                          session: AsyncSession = Depends(get_async_session)):
    return await service.update_employee(session, employee_id, data)


@employee_router.delete("/{employee_id}")
async def delete_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    return await service.delete_employee(session, employee_id)


@employee_router.get("/busy_employees/", response_model=list[EmployeeStructures])
async def get_busy_employees(session: AsyncSession = Depends(get_async_session)):
    return await service.get_busy_employees(session)
