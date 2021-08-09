from flask_testing import TestCase
from flask import url_for 
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_post_string(self):
        gen_pass = "test12"
        response = self.client.post(url_for("post_password"), json=gen_pass)
        text = response.get_json()

        self.assert200(response)
        self.assertEqual(text, 2)
       

