from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    return "<h1>TESTING</h1>"