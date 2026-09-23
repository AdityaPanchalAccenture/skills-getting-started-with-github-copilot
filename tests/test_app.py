from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_duplicate_signup_is_rejected():
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()


def test_unregister_participant_removes_email():
    response = client.delete("/activities/Chess Club/unregister?email=daniel@mergington.edu")

    assert response.status_code == 200
    assert "daniel@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]
