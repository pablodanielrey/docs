from flask import Flask, request
import pytest

@pytest.fixture(scope='module')
def app(request):
    from common import create_app
    app = create_app()
    ctx = app.app_context()
    ctx.push()
    request.addfinalizer(ctx.pop)
    return app

@pytest.fixture(scope='module')
def test_client(request, app):
    client = app.test_client()
    client.__enter__()
    request.addfinalizer(lambda: client.__exit__(None, None, None))
    return client


def test_app_name(app):
    assert app.name == 'common'

def test_welcome_view(text_client):
    rv = test_client.get('/welcome')
    assert 'set-cookie' not in rv.headers
    assert b'Welcome' in rv.data
    assert rv.status_code == 200
 