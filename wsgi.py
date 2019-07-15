from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
	
@application.route("/tamil")
def hellotamil():
    return "vanakam"
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.run(host='0.0.0.0',port=port)