from typing import List, Optional, Tuple
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.types import TaskModel, TaskID, TaskStatus, ModuleInfo
from src.api import tasks
from src.modules import modules_info
import logging

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html><lang="en">
    <head><style>
    h1 {
    margin: 4em;
    text-align: center;
    }
    </style></head>
    <body>
        <h1>TaXAu RPA is Running</h1>
    </body>
    </html>
    """


@app.post("/api/tasks/add", response_model=bool)
async def add_task(task: TaskModel) -> bool:
    logging.info(f"Add Task: {task}")
    return tasks.add(task)


@app.get("/api/tasks/run", response_model=bool)
async def run_task(id: TaskID) -> bool:
    logging.info(f"Run Task: {id}")
    return tasks.run(id)


@app.get("/api/tasks/info", response_model=Optional[List[TaskModel]])
async def get_task_info(id: Optional[TaskID] = None) -> Optional[List[TaskModel]]:
    logging.info(f"Get Task Info: {id}")
    if id is None:
        return tasks.task_info
    else:
        return list(filter(lambda item: item.id == id, tasks.task_info))


@app.get("/api/tasks/status", response_model=Optional[List[Tuple[TaskID, TaskStatus]]])
async def get_task_status(
    id: Optional[TaskID] = None,
) -> Optional[List[Tuple[TaskID, TaskStatus]]]:
    logging.info(f"Get Task Status: {id}")
    if id is None:
        return tasks.task_status
    else:
        return list(filter(lambda item: item[0] == id, tasks.task_status))


@app.get("/api/modules/list", response_model=Optional[List[ModuleInfo]])
async def get_modules_list(
    module_id: Optional[str] = None,
) -> Optional[List[ModuleInfo]]:
    logging.info(f"Get Modules List: {module_id}")
    if module_id is None:
        return modules_info
    else:
        return list(filter(lambda item: item.id == module_id, modules_info))
