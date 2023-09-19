from flask import Flask
from multiplycalc import multiply
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator App!"

@app.route('/multiply/<int:x>/<int:y>')

def multiply_route(x, y):
    result = multiply(x, y)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)