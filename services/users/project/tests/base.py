# services/users/project/tests/base.py


from flask_testing import TestCase

from project import app, db


class BaseTestCase(TestCase):
    def create_app(self): # This one is a must for any Flask Test
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
