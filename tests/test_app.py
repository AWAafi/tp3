import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_square(client):
    response = client.get('/api/square?number=4')
    assert response.status_code == 200
    assert response.json == {'result': 16}
