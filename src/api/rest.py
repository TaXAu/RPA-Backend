from typing import List, Optional, Tuple
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from src.types import TaskModel, TaskID, TaskStatus, ModuleInfo
from src.api import tasks
from src.modules import modules_info

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
    return tasks.add(task)


@app.get("/api/tasks/run", response_model=bool)
async def run_task(id: TaskID) -> bool:
    return tasks.run(id)


@app.get("/api/tasks/info", response_model=Optional[List[TaskModel]])
async def get_task_info(id: Optional[TaskID] = None) -> Optional[List[TaskModel]]:
    if id is None:
        return tasks.task_info
    else:
        return list(filter(lambda item: item.id == id, tasks.task_info))


@app.get("/api/tasks/status", response_model=Optional[List[Tuple[TaskID, TaskStatus]]])
async def get_task_status(id: TaskID) -> Optional[List[Tuple[TaskID, TaskStatus]]]:
    if id is None:
        return tasks.task_status
    else:
        return list(filter(lambda item: item[0] == id, tasks.task_status))


@app.get("/api/modules/list", response_model=Optional[List[ModuleInfo]])
async def get_modules_list(
    module_id: Optional[str] = None,
) -> Optional[List[ModuleInfo]]:
    if module_id is None:
        return modules_info
    else:
        return list(filter(lambda item: item.id == module_id, modules_info))
