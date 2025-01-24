from http import HTTPStatus

import flask

from .app import App
from .rate_limiter import RateLimiter
from .wsgi import StandaloneApplication
from ..utils import (
    LISTEN_HOST,
    SERVER_PORT,
)


_resources = list()


def run_server(host: str = LISTEN_HOST, port: int = SERVER_PORT, redis = None):
    app = App(rate_limiter=RateLimiter(redis))

    for path, function in _resources:
        app.resource(path)(function)
    app.error_resource(HTTPStatus.NOT_FOUND)
    app.error_resource(HTTPStatus.METHOD_NOT_ALLOWED)
    app.error_resource(HTTPStatus.BAD_REQUEST, ValueError)
    app.error_resource(HTTPStatus.INTERNAL_SERVER_ERROR, Exception)
    app.register_collected_resources()

    options = {
        'bind': f'{host}:{port}',
        'max_requests': 200,
        'max_requests_jitter': 20,
    }
    StandaloneApplication(app, options).run()


def collect_resource(path):
    def decorator(function):
        _resources.append((path, function))
        return function
    return decorator


@collect_resource('/')
def user(request: flask.Request, rate_limiter: RateLimiter):
    user_id = request.args.get('clientId')
    if rate_limiter.is_allowed(user_id):
        return 'OK', HTTPStatus.OK
    return 'Service Unavailable', HTTPStatus.SERVICE_UNAVAILABLE


@collect_resource('/ping')
def ping():
    return 'pong', HTTPStatus.OK
