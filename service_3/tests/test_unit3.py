from flask_testing import TestCase
from flask import url_for 
from service_3.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_int(self):
        response = self.client.get(url_for("get_num"))
        
        number_list = [i for i in range(1,100)]

        self.assert200(response)
        self.assertIn(int(response.data.decode()), number_list)