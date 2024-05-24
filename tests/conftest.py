import pytest
from app import create_app, db
from app.models import User


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')
    

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()

            yield testing_client

            db.drop_all()

