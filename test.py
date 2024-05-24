import unittest
from unittest.mock import patch
from main import solver

class TestSolverFunction(unittest.TestCase):

    @patch('builtins.print')
    def test_solver_function(self, mock_print):
        solver(5, 10)
        mock_print.assert_called_with('510')

if __name__ == '__main__':
    unittest.main()
