# services/users/project/__init__.py


from flask import Flask, jsonify


# instantiate the app
app = Flask(__name__)

# set config
# 下面會去讀取
# Users/pat/testdriven.io/testdriven-app/services/users/project/config.py
# class DevelopmentConfig(BaseConfig):
app.config.from_object('project.config.DevelopmentConfig')  # new


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
