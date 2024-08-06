from app.services.security.tokens import create_access_token

test_payload = {
    "user_id": 123,
    "session_id": "session123",
}


def test_create_access_token():
    token = create_access_token(test_payload)
    assert token is not None
    assert isinstance(token, str)
