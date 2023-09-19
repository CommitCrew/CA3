from flask import Flask
from multiply import multipy
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator App!"

@app.route('/multiply/<int:x>/<int:y>')

def multiply_route(x, y):
    result = multipy(x, y)
    return f"The result of {x} * {y} is {result}"

if __name__ == '__main__':
    app.run(debug=True)