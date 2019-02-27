# services/users/manage.py


from flask.cli import FlaskGroup
import unittest

from project import app, db  # new
# to read __init__.py under folder project so it can include variable app and db


cli = FlaskGroup(app)

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
