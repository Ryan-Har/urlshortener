from app import app
from flask import render_template
from flask import request, redirect
import sys
import re

mysqlUser = 'flask'
mysqlPassword = 'q7$L2J9REhiVfJytDgz%'

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/makeurl', methods=['POST', 'GET'])
def sendurl():
    urlRegex = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
    if request.method == "POST":
        input = request.form["input"]
        if re.match(urlRegex, input) is not None:
            return render_template('shortenedurl.html', url = input)
        else:
            return render_template('index.html', error = input, msg = ' is not a valid url')

    #print(uploadURL, file=sys.stderr)
    #print('This is standard output', file=sys.stdout)