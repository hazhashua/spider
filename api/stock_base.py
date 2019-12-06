from flask import Flask
from flask_restful import Api, reqparse, Resource


app = Flask(__name__)
api = Api(app)


# ('/rev/<float:revNo>')
@app.route("/hello_world/<string:arg>")
def hello_world(arg):
    print("hello world, %s" % arg)
    return "hello world, %s" % arg


@app.route("/")
def main():
    return "my fist flast page"

if __name__ == '__main__':
    app.run()