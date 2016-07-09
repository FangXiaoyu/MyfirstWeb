from flask import Flask,request,make_response,redirect,abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	user_agent = request.headers.get('User_Agent')
	return "<h1> Hello World!</h1><p>your browser is %s</p><p>%s</p>"%(user_agent,app.url_map)
@app.route('/user/<name>')
def user(name):
	return '<h1> Hello,%s!</h1>'%name

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

'''
if __name__ == '__main__':
	manager.run()

