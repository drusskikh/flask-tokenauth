from functools import wraps

from flask import current_app,  _request_ctx_stack, session, redirect
from werkzeug.local import LocalProxy


class LoginManager(object):
    load_user = None

    def __init__(self, login_view):
        self.login_view = login_view

    def user_loader(self, callback):
        """Takes token, returns user object."""
        self.user_get = callback

    def init_app(self, app):
        app.login_manager = self
        app.before_request(self._load_user)

    def _load_user(self):
        user = self.load_user(session.get('authtoken'))
        _request_ctx_stack.top.user = user


current_user = LocalProxy(lambda: _request_ctx_stack.top.user)


def login_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if current_user and current_user.is_authenticated():
            return f(*args, **kwargs)
        else:
            return redirect(current_app.login_manager.login_view)


def login_user(user):
    session['authtoken'] = user.login()


def logout_user():
    if 'token' in session:
        del session['authtoken']
    current_user.logout()


class UserMixin(object):

    def is_authenticated(self):
        return True

    def get_id(self):
        raise NotImplementedError()

    def login(self):
        raise NotImplementedError()

    def logout(self):
        raise NotImplementedError()
