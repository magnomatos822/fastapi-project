from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_client():
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"msg": "Teste de FastAPI"}
