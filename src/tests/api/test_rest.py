import json
from fastapi.testclient import TestClient
from src.types import ProgramModel
from src.api.rest import app

client = TestClient(app)


def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_program_model():
    @app.post("/test/program")
    async def get_program_model(program: ProgramModel):
        return program

    with open("src/tests/sample.json", "r") as f:
        data = json.load(f)
    response = client.post("/test/program", json=data)
    assert response.status_code == 200
    assert response.json() == data
