from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    activity_name = "Chess Club"
    email = "student@mergington.edu"

    # Act: sign up the student first
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Act: unregister the same student
    delete_response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert signup_response.status_code == 200
    assert delete_response.status_code == 200

    get_response = client.get("/activities")
    assert get_response.status_code == 200
    assert email not in get_response.json()[activity_name]["participants"]
