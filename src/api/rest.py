from typing import List,Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ActionModel(BaseModel):
    name: str
    id: str
    paras: Dict


class ProgramModel(BaseModel):
    name: str
    id: str
    program: List[ActionModel]


@app.get("/test")
async def test():
    return {"message": "Hello World"}


@app.post("/api/program")
async def exec_program(program: ProgramModel):
    return program


@app.get("api/program/id")
async def get_all_program_id():
    return {"message": "Hello World"}


@app.get("/api/status/{program_id}")
async def get_program_status(program_id: str):
    return {"program_id": program_id}



