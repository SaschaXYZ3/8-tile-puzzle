from AStarQueue import AStarQueue
from Puzzle import Puzzle
import Heuristic
import time


def main():
    # Create a puzzle object
    puzzle = Puzzle()  # A random but solvable game board is created here

    # Show the current puzzle
    print("Aktuelles Puzzle (Gameboard):")
    puzzle.printGameBoard()

    # Calculate the Manhattan distance
    manhattan = Heuristic.ManhattanDistance(puzzle)
    manhattan_cost = manhattan.calculate(puzzle.gameBoard)
    print(f"Manhattan Distance: {manhattan_cost}")

    # Calculate the Hamming distance
    hamming = Heuristic.HammingDistance(puzzle)
    hamming_cost = hamming.calculate(puzzle.gameBoard)
    print(f"Hamming Distance: {hamming_cost}")

    # Check whether the goal has been achieved
    if puzzle.isGoalReached():
        print("Das Puzzle hat das Ziel erreicht!")
    else:
        print("Das Ziel wurde noch nicht erreicht.")

        # Run A* algorithm to solve the puzzle
        # We can use the Manhattan distance or the Hamming distance as a heuristic here
        heuristic = Heuristic.ManhattanDistance(puzzle)  # Select the heuristic (Manhattan or Hamming)
        queue = AStarQueue(heuristic)  # Initialize the AStarQueue (A* algorithm)

        # Find the solution to the puzzle
        start_time = time.time()
        queue.findSolution()
        end_time = time.time()

        # Output of the solution path
        print("\nLösungspfad:")
        queue.printPath()

        # Show the number of steps needed to solve the puzzle
        print(f"Anzahl der Schritte: {queue.numberOfMoves}")

        # Output the runtime
        print(f"Berechnungszeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()