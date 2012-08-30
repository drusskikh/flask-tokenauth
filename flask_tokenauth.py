from functools import wraps

from flask import current_app,  _request_ctx_stack, session, redirect, url_for, request
from werkzeug.local import LocalProxy


class LoginManager(object):
    user_callback = None

    def __init__(self, login_view):
        self.login_view = login_view

    def user_loader(self, callback):
        """Takes token, returns user object."""
        self.user_callback = callback

    def init_app(self, app):
        app.login_manager = self
        app.before_request(self._load_user)

    def _load_user(self):
        authtoken = session.get('authtoken')
        if authtoken:
            user = self.user_callback(authtoken)
        else:
            user = None
        _request_ctx_stack.top.user = user


current_user = LocalProxy(lambda: _request_ctx_stack.top.user)


def login_required(f):
    @wraps(f)
    def decorated_view(*args, **kwargs):
        if current_user:
            return f(*args, **kwargs)
        else:
            login_view = current_app.login_manager.login_view
            return redirect(url_for(login_view, next=request.path))
    return decorated_view


def login_user(user):
    session['authtoken'] = user.login()


def logout_user():
    if 'authtoken' in session:
        authtoken = session.pop('authtoken')
        current_user.logout(authtoken)


class UserMixin(object):

    def get_id(self):
        raise NotImplementedError()

    def login(self):
        """Returns auth token."""
        raise NotImplementedError()

    def logout(self, authtoken):
        """Takes authtoken."""
        raise NotImplementedError()
