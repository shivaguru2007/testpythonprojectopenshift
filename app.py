from flask import Flask
from flask import render_template
import os
from main.forms import LoginForm
application = Flask(__name__)
from main.config import config

SECRET_KEY = os.urandom(32)
application.config['SECRET_KEY'] = SECRET_KEY


@application.route("/")
def hello():
	list1 = ['python','java','c++']
	return render_template('footer.html',user="shiva",list1=list1)
    
@application.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == config.USERNAME and form.password.data == config.PASSWORD:
			return "user authenticated."
	return render_template('loginpage.html',form=form)

	
@application.route("/tamil")
def hellotamil():
    return "vanakam"
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.run(host='0.0.0.0',port=port)