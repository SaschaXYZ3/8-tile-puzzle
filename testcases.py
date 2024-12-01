import unittest
from Puzzle import Puzzle
from AStarQueue import AStarQueue
import Heuristic


class TestPuzzle(unittest.TestCase):
    def test_is_solvable(self):
        # Solvable puzzle
        solvable_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.assertTrue(Puzzle.isSolvable(solvable_board))

        # Unsolvable puzzle
        unsolvable_board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
        self.assertFalse(Puzzle.isSolvable(unsolvable_board))

    def test_is_goal_reached(self):
        # Goal state
        puzzle = Puzzle(gameBoard=[[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertTrue(puzzle.isGoalReached())

        # Non-goal state
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        self.assertFalse(puzzle.isGoalReached())

    def test_generate_possible_moves(self):
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 0, 5], [6, 7, 8]])
        possible_moves = puzzle.generatePossibleMoves()
        self.assertEqual(len(possible_moves), 4)  # 4 possible moves for the blank tile
        self.assertIn([[1, 0, 3], [4, 2, 5], [6, 7, 8]], possible_moves)

    def test_manhattan_distance(self):
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 5, 6], [0, 7, 8]])
        heuristic = Heuristic.ManhattanDistance(puzzle)
        self.assertEqual(heuristic.calculate(puzzle.gameBoard), 2)

    def test_hamming_distance(self):
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 5, 6], [0, 8, 7]])
        heuristic = Heuristic.HammingDistance(puzzle)
        self.assertEqual(heuristic.calculate(puzzle.gameBoard), 2)


class TestAStarQueue(unittest.TestCase):
    def test_find_solution_manhattan(self):
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 5, 6], [0, 7, 8]])
        heuristic = Heuristic.ManhattanDistance(puzzle)
        queue = AStarQueue(puzzle, heuristic)
        queue.findSolution()
        self.assertEqual(queue.numberOfMoves, 2)  # It should take 2 moves to solve

    def test_find_solution_hamming(self):
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 5, 6], [0, 8, 7]])
        heuristic = Heuristic.HammingDistance(puzzle)
        queue = AStarQueue(puzzle, heuristic)
        queue.findSolution()
        self.assertEqual(queue.numberOfMoves, 2)  # It should take 2 moves to solve

    def test_expand_node(self):
        puzzle = Puzzle(gameBoard=[[1, 2, 3], [4, 0, 5], [6, 7, 8]])
        heuristic = Heuristic.ManhattanDistance(puzzle)
        queue = AStarQueue(puzzle, heuristic)
        queue.setFirstNode()
        queue.expandNode(0)
        self.assertEqual(len(queue.nodes), 5)  # 1 parent node and 4 child nodes


if __name__ == "__main__":
    unittest.main()