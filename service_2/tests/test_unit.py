from flask_testing import TestCase
from flask import url_for 
from app import app, string_list

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPost(TestBase):

    def test_post_string(self):
        pass_length = 5
        response = self.client.post(url_for("post_string"), json=pass_length)
        text = response.data.decode()

        def check_letters(text):
            status = True
            for i in text:
                if i not in string_list:
                    status = False 
            return status

        self.assert200(response)
        self.assertEqual(len(text), 3)
        self.assertEqual(check_letters(text), True)

