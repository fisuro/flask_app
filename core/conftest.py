from core import app
from core.models import db
import pytest

@pytest.fixture
def client():
    db.drop_all()
    db.create_all()
    return app.test_client()