import unittest
from flask import url_for
import pytest
import urllib2
from FlaskBasicAppWithConfig import create_app 
from config import DevelopmentConfig

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(DevelopmentConfig)
    return app

@pytest.mark.usefixtures('live_server')
class TestLiveServer:

  def test_flask_application_is_up_and_running(self):
    response = urllib2.urlopen(url_for('hello_world', _external=True))
    assert response.code == 200

if __name__ == '__main__':
    unittest.main()
