from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def get_all():
    response = client.get("/animals")
    assert response.status_code == 200

get_all()