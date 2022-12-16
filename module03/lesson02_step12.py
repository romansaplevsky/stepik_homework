import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        assert abs(-42) == 42, "Should be absolute of a number"

    def test_abs2(self):
        assert abs(-42) == -42, "Should be absolute of a number"


if __name__ == "__main__":
    unittest.main()