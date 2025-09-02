import unittest
import io
import sys
from main import hello_world


class TestMain(unittest.TestCase):
    def test_hello_world(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, World!\n")


if __name__ == '__main__':
    unittest.main()
