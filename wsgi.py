from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
	
@application.route("/tamil")
def hellotamil():
    return "vanakam"
	

if __name__ == "__main__":
    application.run()