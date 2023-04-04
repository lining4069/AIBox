from flask import Flask
from contorller.mulMessage import mul_message
from contorller.mulMessageByAPI2D import mul_message_api2d

app = Flask(__name__)
app.register_blueprint(mul_message)
app.register_blueprint(mul_message_api2d)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
