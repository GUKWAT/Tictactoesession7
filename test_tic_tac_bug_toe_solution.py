import unittest

from tic_tac_bug_toe_solution import tally_wins


class TestTicTacToe(unittest.TestCase):

    def test_tally_wins(self):
        results = [True, False, True]
        self.assertEqual(tally_wins(results), 2)


# This allows running the tests by running the script
if __name__ == '__main__':
    unittest.main()
