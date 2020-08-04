import unittest

from bysh.core import Engine


class TestBysh(unittest.TestCase):
    def test_ast_loading(self):
        bsh = Engine()
        self.assertIsNone(bsh.current_ast)
        bsh.load_ast(['ast'])
        self.assertEqual(['ast'], bsh.current_ast)


if __name__ == '__main__':
    unittest.main()
