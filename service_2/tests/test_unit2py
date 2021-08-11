from flask_testing import TestCase
from flask import url_for 
from service_2.app import app, string_list

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_post_string(self):
        pass_length = 5
        response = self.client.post(url_for("post_string"), json=pass_length)

        def check_letters(text):
            status = True
            for i in text:
                if i not in string_list:
                    status = False 
            return status

        self.assert200(response)
        self.assertEqual(len(response.data.decode()), 3)
        self.assertEqual(check_letters(response.data.decode()), True)

