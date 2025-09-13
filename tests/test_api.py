from fastapi.testclient import TestClient
from super_expert_comptable_v04.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Bienvenue sur l'API Super Expert Comptable v04"}
