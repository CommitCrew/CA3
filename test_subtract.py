from flask_calculator import app


def test_subtract():
    with app.test_client() as client:
        response = client.get('/subtract/6/3')
        assert response.get_data(as_text=True) == '3'

