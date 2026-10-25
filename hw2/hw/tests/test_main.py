from fastapi.testclient import TestClient
from shop_api.main import app

client = TestClient(app)

def metrics_available() -> None:
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
