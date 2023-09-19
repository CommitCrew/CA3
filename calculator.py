from flask import Flask
from CA3.hello import add
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Calculator App!'

@app.route('/add/<int:x>/<int:y>')
def add_route(x,y):
    result = add(x,y)
    return f"The result of {x} + {y} is {result}"

if __name__ == '__main__':
    app.run(debug=True)