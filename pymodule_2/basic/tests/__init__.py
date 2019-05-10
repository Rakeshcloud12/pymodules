import logging

from flask_testing import TestCase

from basic import init_api


class BaseTestCase(TestCase):
    @staticmethod
    def create_app():
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = init_api()
        return app.app

    @staticmethod
    def base_url(url):
        return f"/v2/basic/{url}"
