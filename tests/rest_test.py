import contextlib
import subprocess
import time

import requests
import pytest


@pytest.fixture(scope='module')
def rest_plus_redis():
    subprocess.call('./scripts/run_docker_compose.sh')
    _wait_for_healthy()
    yield
    subprocess.call('./scripts/stop_docker_compose.sh')


def test_ping(rest_plus_redis):
    assert requests.get('http://localhost:8080/ping').json() == 'pong'


def test_user(rest_plus_redis):
    assert requests.get('http://localhost:8080/?clientId=0').status_code == 200


def test_unavailable_logic(rest_plus_redis):
    assert requests.get('http://localhost:8080/?clientId=1').status_code == 200
    assert requests.get('http://localhost:8080/?clientId=1').status_code == 200
    assert requests.get('http://localhost:8080/?clientId=1').status_code == 200
    assert requests.get('http://localhost:8080/?clientId=1').status_code == 200
    assert requests.get('http://localhost:8080/?clientId=1').status_code == 200
    assert requests.get('http://localhost:8080/?clientId=1').status_code == 503


def _wait_for_healthy():
    sec = 0
    timeout = 30
    interval = 0.5
    while sec < timeout:
        with contextlib.suppress(requests.ConnectionError):
            response = requests.get('http://localhost:8080/ping')
            if response.status_code:
                break
        time.sleep(interval)
        sec += interval
    else:
        raise Exception('Session failed to connect rest server')
