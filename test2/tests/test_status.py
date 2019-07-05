import os
import tempfile

import pytest

from status_app import main


@pytest.fixture
def client():
    """Set up test client."""
    os.environ['APP_VERSION'] = "1.0"
    os.environ['COMMIT_SHA'] = "aaaa"
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()
    yield client

def test_empty_db(client):
    """Test the status end point.."""

    rv = client.get('/status')
    assert b'"version": "1.0"' in rv.data
    assert b'"lastcommitsha": "aaaa"' in rv.data
    assert b'"description" : "pre-interview technical test"' in rv.data
