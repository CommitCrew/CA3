from calculator import app
from flask import jsonify
def test_multiply():
    with app.test_client() as client:
        response = client.get('/multiply/2/3')
        assert response.get_data(as_text=True) == "6"
