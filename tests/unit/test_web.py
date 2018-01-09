import os
from flask import Flask, url_for
import pytest
import yaml

from web import create_app, load_config


@pytest.fixture
def app():
    app = create_app()
    return app


def test_app(client):
    response = client.get(url_for('api.index'))
    assert response.status_code == 200
    name = os.environ.get('HELLO_NAME') or load_config('name')
    assert 'hello ' + name in str(response.data)
    assert 'fail' not in str(response.data)

def test_time_view(client):
    response = client.get(url_for('timeApi.index'))
    assert response.status_code == 200
    assert 'Hello world!' in str(response.data)
    assert 'This is a test view to show the current time' in str(response.data)
    assert 'host' in str(response.data)
    assert 'time' in str(response.data)
    assert 'fail' not in str(response.data)
    