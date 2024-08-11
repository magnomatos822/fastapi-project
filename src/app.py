from http import HTTPStatus

from fastapi import FastAPI

from src.schemas import Message
from src.userSchemas import Users

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"msg": "Teste de FastAPI"}

@app.post("/users", status_code=HTTPStatus.CREATED, response_model=Users)
def create_user(user: Users):
    return user