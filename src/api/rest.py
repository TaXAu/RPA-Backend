from typing import List, Optional, Tuple
from fastapi import FastAPI
from src.types import TaskModel, TaskID, TaskStatus
from src.task import TaskQueue

app = FastAPI()
tasks = TaskQueue()


@app.post("/api/tasks/add", response_model=bool)
async def add_task(task: TaskModel) -> bool:
    return tasks.add(task)


@app.get("/api/tasks/info", response_model=Optional[List[TaskModel]])
async def get_task_info(id: Optional[TaskID] = None) -> Optional[List[TaskModel]]:
    if id is None:
        return tasks.task_info
    elif id is TaskID:
        return list(filter(lambda item: item.id == id, tasks.task_info))
    else:
        return None


@app.get("/api/tasks/status", response_model=Optional[List[Tuple[TaskID, TaskStatus]]])
async def get_task_status(id: TaskID) -> Optional[List[Tuple[TaskID, TaskStatus]]]:
    if id is None:
        return tasks.task_status
    elif id is TaskID:
        return list(filter(lambda item: item[0] == id, tasks.task_status))
    else:
        return None
