import pytest
from fastapi.testclient import TestClient

from app.main import app

@pytest.fixture
def client():
    """
    Docstring for client
    client를 fixture로 설정
    """
    return TestClient(app)

@pytest.fixture
def session_data_set_up(client):
    client.post('/__test__/session/mock')
    return client