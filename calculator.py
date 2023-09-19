from flask import Flask
from hello import add
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Calculator App!'

@app.route('/add/<int:x>/<int:y>')
def add_route(x,y):
    result = add(x,y)
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)