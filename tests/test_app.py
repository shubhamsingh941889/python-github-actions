from run import app
import unittest

class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual("Hello World 12345", response.text)

if __name__ == "__main__":
    unittest.main()