from flask_testing import TestCase
from flask import url_for

from service_1.application import app, db
from service_1.application.models import Password

from os import getenv

import requests_mock

class TestBase(TestCase):
    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI= "sqlite:///test.db",
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            WTF_CSRF_ENABLED = False,
            SECRET_KEY = getenv("SECRET_KEY")
        )
        
        return app

    def setUp(self):
        db.create_all()

        db.session.add(Password(password="test13", pass_score="2"))
        db.session.commit()

    def tearDown(self):
        db.drop_all()


class TestRead(TestBase):
    def test_index(self):
        response = self.client.get(url_for("index"))
        assert "1 | test13 | 2 | Not in Use |" in response.data.decode()

class TestCreate(TestBase):
    def test_create(self):
        response = self.client.get(url_for("create"))
        self.assertEqual(response.status_code, 200)
        
        with requests_mock.mock() as m:
            
            m.post("http://service-2:5000/post/string", text="test")
            m.get("http://service-3:5000/get/num", text="14")
            m.post("http://service-4:5000/post/password", json=2)

            response = self.client.post(
                url_for("create"),
                data = dict(pass_length= 5),
                follow_redirects = True
            )

        response2 = self.client.get(url_for("index"))

        self.assert200(response2)
        self.assertIn("2 | test14 | 2 | Not in Use |", response2.data.decode()) 
 
class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.get(url_for("update", id = 1),
        follow_redirects = True)

        assert "1 | test13 | 2 | In Use |" in response.data.decode()

        response = self.client.get(url_for("update", id = 1),
        follow_redirects = True)

        assert "1 | test13 | 2 | Not in Use |" in response.data.decode()


class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(url_for("delete", id = 1),
        follow_redirects = True)

        assert "1 | test13 | 2 | Not in Use |" not in response.data.decode()