from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from task import service
from task.structures import TaskStructures, TaskCreateStructures

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])


@tasks_router.get("/", response_model=list[TaskStructures], status_code=status.HTTP_200_OK)
async def get_all_tasks(session: AsyncSession = Depends(get_async_session)):
    return await service.get_all_tasks(session)


@tasks_router.post("/", response_model=TaskStructures, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreateStructures, session: AsyncSession = Depends(get_async_session)):
    return await service.create_task(session, task)


@tasks_router.get("/{task_id}", response_model=TaskStructures, status_code=status.HTTP_200_OK)
async def get_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    return await service.get_task_by_id(session, task_id)


@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    return await service.delete_task(session, task_id)


@tasks_router.put("/{task_id}", response_model=TaskStructures, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, data: TaskCreateStructures, session: AsyncSession = Depends(get_async_session)):
    return await service.update_task(session, task_id, data)
