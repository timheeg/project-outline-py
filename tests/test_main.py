import unittest

from src import main


class TestMain(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(main.is_true())

    def test_is_false(self):
        self.assertFalse(main.is_false())


if __name__ == "__main__":
    unittest.main()
