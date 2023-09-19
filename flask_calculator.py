from flask import Flask
from subtractftn import subtract
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Calculator App!"

@app.route('/subtract/<int:x>/<int:y>')
def subtract_route(x, y):
    result = subtract(x, y)
    return f"The result of {x} - {y} is {result}"

if __name__ == '__main__':
    app.run(debug=True)
