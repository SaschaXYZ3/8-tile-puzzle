import unittest  # For the test framework
from Puzzle import Puzzle  # To test puzzle-related functionality
from AStarQueue import AStarQueue  # To test the A* algorithm implementation
import Heuristic  # To test Manhattan and Hamming heuristic calculations
from main import compare_heuristics  # To test heuristic comparison functionality

class TestPuzzle(unittest.TestCase):
    def test_random_puzzle_solvability(self):
        """Test that random puzzles generated are solvable."""
        for _ in range(10):  # Test 10 random puzzles
            puzzle = Puzzle()
            self.assertTrue(puzzle.isSolvable(puzzle.gameBoard), "Generated puzzle is not solvable!")

    def test_specific_solvable_puzzle(self):
        """Test a specific solvable puzzle."""
        solvable_puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Solved state
        self.assertTrue(solvable_puzzle.isSolvable(solvable_puzzle.gameBoard),
                        "Specific solvable puzzle marked as unsolvable!")

    def test_specific_unsolvable_puzzle(self):
        """Test a specific unsolvable puzzle."""
        unsolvable_puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [8, 7, 0]])  # Inversions make it unsolvable
        self.assertFalse(unsolvable_puzzle.isSolvable(unsolvable_puzzle.gameBoard),
                         "Specific unsolvable puzzle marked as solvable!")

    def test_goal_state_detection(self):
        """Test if the goal state is correctly detected."""
        solved_puzzle = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertTrue(solved_puzzle.isGoalReached(), "Goal state not detected as solved!")

        unsolved_puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
        self.assertFalse(unsolved_puzzle.isGoalReached(), "Unsolved puzzle detected as solved!")


class TestAStarQueue(unittest.TestCase):
    def test_astar_with_manhattan(self):
        """Test A* with Manhattan heuristic on a solvable puzzle."""
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Already solved
        heuristic = Heuristic.ManhattanDistance(puzzle)
        queue = AStarQueue(heuristic)
        queue.findSolution()
        self.assertEqual(queue.numberOfMoves, 0, "Solved puzzle should require 0 moves!")

    def test_astar_with_hamming(self):
        """Test A* with Hamming heuristic on a solvable puzzle."""
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Already solved
        heuristic = Heuristic.HammingDistance(puzzle)
        queue = AStarQueue(heuristic)
        queue.findSolution()
        self.assertEqual(queue.numberOfMoves, 0, "Solved puzzle should require 0 moves!")

    def test_astar_solution_path(self):
        """Test that A* produces the correct solution path."""
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])  # One move away
        heuristic = Heuristic.ManhattanDistance(puzzle)
        queue = AStarQueue(heuristic)
        queue.findSolution()
        self.assertEqual(queue.numberOfMoves, 1, "Puzzle should require 1 move to solve!")


class TestHeuristics(unittest.TestCase):
    def test_manhattan_distance(self):
        """Test Manhattan distance calculation."""
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Solved state
        heuristic = Heuristic.ManhattanDistance(puzzle)
        self.assertEqual(heuristic.calculate(puzzle.gameBoard), 0, "Manhattan distance for solved puzzle should be 0!")

        scrambled_puzzle = Puzzle([[1, 2, 3], [4, 6, 5], [7, 8, 0]])  # One tile misplaced
        heuristic = Heuristic.ManhattanDistance(scrambled_puzzle)
        self.assertEqual(heuristic.calculate(scrambled_puzzle.gameBoard), 2, "Manhattan distance mismatch!")

    def test_hamming_distance(self):
        """Test Hamming distance calculation."""
        puzzle = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Solved state
        heuristic = Heuristic.HammingDistance(puzzle)
        self.assertEqual(heuristic.calculate(puzzle.gameBoard), 0, "Hamming distance for solved puzzle should be 0!")

        scrambled_puzzle = Puzzle([[1, 2, 3], [4, 6, 5], [7, 8, 0]])  # Two tiles misplaced
        heuristic = Heuristic.HammingDistance(scrambled_puzzle)
        self.assertEqual(heuristic.calculate(scrambled_puzzle.gameBoard), 2, "Hamming distance mismatch!")


class TestHeuristicComparison(unittest.TestCase):
    def test_heuristic_comparison(self):
        """Test heuristic comparison functionality."""
        try:
            compare_heuristics(num_trials=2)
        except Exception as e:
            self.fail(f"Heuristic comparison failed with exception: {e}")

