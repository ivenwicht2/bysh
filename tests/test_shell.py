import unittest
from bysh import Shell


class TestShell(unittest.TestCase):
    def test_instance(self):
        sh = Shell()
        self.assertIsNotNone(sh)


if __name__ == '__main__':
    unittest.main()
