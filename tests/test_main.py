from main import app
from unittest.mock import  patch

test_data = {'emp': 100, 'job': 'Admin', 'year': 2010}


@patch('main.firestore.Client')
def test_get_emp(mock_fire):
    mock_fire.return_value.collection.return_value.document.return_value.get.return_value.to_dict.return_value = test_data
    with app.test_client() as c:
        response = c.get('/api/v1/resources/employee/1000')
        assert response.status_code == 200
        assert response.get_json() == test_data
