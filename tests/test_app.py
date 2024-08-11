from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_client():
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"msg": "Teste de FastAPI"}

def test_create_user():
    client = TestClient(app)

    response = client.post("/users", json={"name": "Teste",
                            "email": "teste@teste", 
                            "password": "1234"},
                            status_code=HTTPStatus.CREATED)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "Teste", 
        "email": "teste@teste", 
        "password": "1234"
        }
{
    "name": "Teste", 
    "email": "teste@teste", 
    "password": "1234"
    "password": "1234"
    "password": "1234"
}