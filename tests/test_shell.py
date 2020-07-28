import unittest
from bysh.core.shell import Shell


class TestShell(unittest.TestCase):
    def test_instance(self):
        sh = Shell(None, None)
        self.assertIsNotNone(sh)


if __name__ == '__main__':
    unittest.main()
