"""
Microservice Test Module
This module defines a simple microservice using Flask, a lightweight web framework for Python.
It provides two endpoints:
- /api/hello: Returns a JSON response with a greeting message.
- /api/add: Accepts two numbers as query parameters and returns their sum.

"""
import unittest
import requests

class TestMicroservice(unittest.TestCase):
    def test_add_endpoint(self):
        """
        Handle GET request for /api/add endpoint.
        Accepts two numbers as query parameters and returns their sum.
        Returns:
            JSON response with the sum of two numbers.
        """
        response = requests.get('http://127.0.0.1:5000/api/add?num1=3&num2=5')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 8)

if __name__ == '__main__':
    unittest.main()
