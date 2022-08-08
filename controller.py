from . import User, render_template


def list():
    users = [
        User(name='aaa', email='aaa@gmail.com')
        User(name='bbb', email='bbb@gmail.com')
        User(name='ccc', email='ccc@gmail.com')
    ]
    return render_template('./views.html', {users: users})
