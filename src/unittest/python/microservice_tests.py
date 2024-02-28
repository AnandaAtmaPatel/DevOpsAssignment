import unittest
import requests

class TestMicroservice(unittest.TestCase):
    def test_add_endpoint(self):
        response = requests.get('http://127.0.0.1:5000/api/add?num1=3&num2=5')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 8)

if __name__ == '__main__':
    unittest.main()
