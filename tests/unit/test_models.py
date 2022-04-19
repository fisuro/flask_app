from core.models import User

def test_new_user():
    user = User('Filip', 'Bjelic', 'fisuro@gmail.com')
    assert user.name == 'Filip'
    assert user.surname == 'Bjelic'
    assert user.email == 'fisuro@gmail.com'