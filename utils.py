from AStarQueue import AStarQueue

def display_board(puzzle):
    """Display the current gameboard."""
    print("Current Puzzle (Gameboard):")
    puzzle.printGameBoard()



def solve_puzzle(puzzle, heuristic_class):
    """
    Solve the puzzle using A* with the given heuristic class.

    Args:
        puzzle (Puzzle): The initial puzzle to solve.
        heuristic_class (type): The heuristic class to use (e.g., ManhattanDistance).
    """
    heuristic_instance = heuristic_class(puzzle)  # Initialize the heuristic
    queue = AStarQueue(puzzle, heuristic_instance)  # Initialize the AStarQueue
    queue.findSolution()  # Solve the puzzle

    print("\nSolution path:")
    queue.printPath()  # Display the solution path
    print(f"Number of Moves required: {queue.numberOfMoves}")