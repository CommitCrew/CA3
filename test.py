from calculator import app

def test_add():
    with app.test_client() as client:
        response = client.get('/add/4/2')
        assert response.get_data(as_text=True) == '6'