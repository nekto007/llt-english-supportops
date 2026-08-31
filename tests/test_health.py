from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app, follow_redirects=False)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200 and response.json() == {"status": "ok", "service": "supportops"}
