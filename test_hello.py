import unittest
from hello import greet

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), "Hi!")
