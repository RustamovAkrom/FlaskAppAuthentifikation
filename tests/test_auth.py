import pytest
from app.models import User


def test_login_page(test_client):
    response = test_client.get('/login')

    assert response.status_code == 200
    assert b"Sign In" in response.data

