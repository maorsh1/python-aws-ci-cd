from flask import Flask

application = Flask(__name__)

@application.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
