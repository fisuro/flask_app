from core.conftest import client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_routes(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == []

    response = client.get('/something')
    assert response.status_code == 404

    response = client.post('/users', json={"name":"filip", "surname":"bjelic", "email":"fisurogmail.com"})
    assert response.status_code == 400

    response = client.post('/users', json={"name":"filip", "surname":"bjelic", "email":"fisuro@gmail.com"})
    assert response.status_code == 200
    assert response.json == {"name":"filip", "surname":"bjelic", "email":"fisuro@gmail.com"}