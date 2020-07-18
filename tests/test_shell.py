import unittest
from bysh.shell import Shell


class TestShell(unittest.TestCase):
    def test_instance(self):
        sh = Shell()
        self.assertIsNotNone(sh)
        self.assertIsNotNone(sh.stdin)
        self.assertIsNotNone(sh.stdout)
        self.assertIsNotNone(sh.stderr)


if __name__ == '__main__':
    unittest.main()
