from flask import Flask
from flask import render_template
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('templates/index.html',user="shiva")
	
@application.route("/tamil")
def hellotamil():
    return "vanakam"
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.run(host='0.0.0.0',port=port)