from app import app
from flask import render_template

mysqlUser = 'flask'
mysqlPassword = 'q7$L2J9REhiVfJytDgz%'

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    return render_template('index.html')

