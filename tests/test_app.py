from app import app

from litestar.testing import TestClient


def test_sync() -> None:
    with TestClient(app=app) as client:
        assert client.get("/sync").json() == {"hello": "world"}


def test_async() -> None:
    with TestClient(app=app) as client:
        assert client.get("/async").json() == {"hello": "world"}
