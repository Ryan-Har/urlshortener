from app import app, dbfunction
from flask import render_template
from flask import request, redirect
import sys
import re

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    urlRegex = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
    if request.method == "POST":
        input = str(request.form["input"])
        if re.match(urlRegex, input) is not None:
            generatedId = dbfunction.getID()
            dbfunction.addUrl(generatedId, input)
            return render_template('shortenedurl.html', url = generatedId)
        else:
            return render_template('index.html', error = input, msg = ' is not a valid url')    
    else:
        return render_template('index.html')

@app.route('/<shorturl>')
def forward(shorturl):
    if dbfunction.checkIfIdExists(shorturl):
        longurl = dbfunction.getUrl(shorturl)
        slicedLongUrl = longurl[2:-3] #sliced to get usable url. Unable to get this working in the function
        return redirect(slicedLongUrl)
    else:
        return render_template('index.html', error = shorturl, msg = 'is not a valid extension')
