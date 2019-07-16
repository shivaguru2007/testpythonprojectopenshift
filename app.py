from flask import Flask
from flask import render_template
import os
application = Flask(__name__)

@application.route("/")
def hello():
	list1 = ['python','java','c++']
	return render_template('footer.html',user="shiva",list1=list1)
    
	
@application.route("/tamil")
def hellotamil():
    return "vanakam"
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.run(host='0.0.0.0',port=port)