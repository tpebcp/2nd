# services/users/manage.py

import unittest

from flask.cli import FlaskGroup

from project import create_app, db  # new
from project.api.models import User  # new

# to read __init__.py under folder project so it can include variable app and db

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new


# new
# This registers a new command, recreate_db, to the CLI 
# so that we can run it from the command line, which we'll use shortly to apply the model to the database
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
