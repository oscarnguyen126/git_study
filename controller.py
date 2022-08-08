from util import render_template
from db import users
from model import User


def list():
    return render_template('./views.html', {users: users})


def register(request):
    username, email, password, password_repeat = request.data
    if password == password_repeat:
        User(username, email, password)
    else:
        raise Error('passwords are not matched')


def login_user(request):
    username, password = request.data
    current_user = None
    for user in users:
        if user.name == username:
            current_user = user

    if not current_user:
        raise Error('User not found')

    is_valid_password = current_user.validate_password(password)
    if not is_valid_password:
        raise Error('Wrong password')
    
    return current_user
