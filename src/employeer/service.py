from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy import select, delete, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from employeer.models import EmployeerModel
from employeer.structures import EmployeeStructures


async def get_all_employees(db: AsyncSession):
    res = await db.execute(select(EmployeerModel))
    return res.scalars().all()


async def get_employee_by_id(db: AsyncSession, employee_id: int):
    res = await db.execute(select(EmployeerModel).filter(EmployeerModel.id == employee_id))
    return res.scalars().one()


async def create_employee(db: AsyncSession, data: EmployeeStructures):
    employee = EmployeerModel(**data.model_dump())
    try:
        db.add(employee)
        await db.commit()
    except ValidationError as err:
        raise HTTPException(status_code=400, detail=err.messages)
    return JSONResponse(content={'message': 'Employee created'}, status_code=status.HTTP_201_CREATED)


async def update_employee(db: AsyncSession, employee_id: int, data: EmployeeStructures):
    query = (update(EmployeerModel).filter(EmployeerModel.id == employee_id).values(**data.model_dict())
             .returning(EmployeerModel))
    try:
        res = await db.execute(query)
        await db.commit()
    except IntegrityError as e:
        await db.rollback()
        raise e
    return res.scalars().one()


async def delete_employee(db: AsyncSession, employee_id: int):
    query = delete(EmployeerModel).filter(EmployeerModel.id == employee_id)
    await db.execute(query)
    await db.commit()
    return {'status': status.HTTP_200_OK}
