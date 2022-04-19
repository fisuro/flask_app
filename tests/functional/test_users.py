from core import app
from core.models import db


def create_app():
    db.drop_all()
    db.create_all()
    return app

def test_home_page():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_routes():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/users')
        assert response.status_code == 200
        assert response.json == []

    with flask_app.test_client() as test_client:
        response = test_client.get('/something')
        assert response.status_code == 404

    with flask_app.test_client() as test_client:
        response = test_client.post('/users', json={"name":"filip", "surname":"bjelic", "email":"fisurogmail.com"})
        assert response.status_code == 400

    with flask_app.test_client() as test_client:
        response = test_client.post('/users', json={"name":"filip", "surname":"bjelic", "email":"fisuro@gmail.com"})
        assert response.status_code == 200
        assert response.json == {"name":"filip", "surname":"bjelic", "email":"fisuro@gmail.com"}