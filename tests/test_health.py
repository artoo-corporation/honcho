"""Smoke tests for public health endpoint."""

from fastapi.testclient import TestClient


async def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
