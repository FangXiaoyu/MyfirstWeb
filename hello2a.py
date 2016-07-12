from flask import Flask,request,make_response,redirect,abort,render_template,session,url_for,flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class NameForm(Form):
	name = StringField('What is your name?',validators = [Required()])
	submit = SubmitField('Submit')

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

@app.route('/agent')
def agent():
	user_agent = request.headers.get('User_Agent')
	return "<h1> Hello World!</h1><p>your browser is %s</p><p>%s</p>"%(user_agent,app.url_map)



@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html',current_time = datetime.utcnow(),form = form,name = session.get('name'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name = name)



@app.route('/test1')
def test1():
	return '<h1>Bad request</h1>',400

@app.route('/test2')
def test2():
	response = make_response('<h1>this document carries a cookie!</h1>')
	response.set_cookie('answer','42')
	return response

@app.route('/test3')
def test3():
	return redirect('http://localhost:5000')



'''
@app.route('/user/<int:id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>hello.%s</h1>' % user.name

don't worry it's just a test

'''
if __name__ == '__main__':
	manager.run()

