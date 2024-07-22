import unittest
from app.application import application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b"Hello, World!")

if __name__ == "__main__":
    unittest.main()
\