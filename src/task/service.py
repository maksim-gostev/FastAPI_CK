from fastapi import status
from sqlalchemy import select, delete, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from task.models import TasksModel
from task.structures import TaskCreateStructures


async def get_all_tasks(db: AsyncSession):
    res = await db.execute(select(TasksModel).order_by(TasksModel.id))
    return res.scalars().all()


async def get_task_by_id(db: AsyncSession, task_id: int):
    res = await db.execute(select(TasksModel).filter(TasksModel.id == task_id))
    return res.scalars().one()


async def create_task(db: AsyncSession, data: TaskCreateStructures):
    task = TasksModel(**data.model_dump())
    try:
        db.add(task)
        await db.commit()
    except IntegrityError as e:
        await db.rollback()
        raise e
    return task


async def update_task(db: AsyncSession, task_id: int, data: TaskCreateStructures):
    query = (update(TasksModel).filter(TasksModel.id == task_id)
             .values(**data.model_dump()).returning(TasksModel))
    try:
        res = await db.execute(query)
        await db.commit()
    except IntegrityError as e:
        await db.rollback()
        raise e
    return res.scalars().one()


async def delete_task(db: AsyncSession, task_id: int):
    try:
        query = (delete(TasksModel).filter(TasksModel.id == task_id)
                 .execution_options(synchronize_session='fetch'))
        await db.execute(query)
        await db.commit()
        return {"status": status.HTTP_200_OK}
    except IntegrityError:
        return (
            {
                "error": "Эту задачу нельзя удалить",
                'status': status.HTTP_405_METHOD_NOT_ALLOWED
            },
        )
