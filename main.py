from Puzzle import Puzzle
from utils import display_board, solve_puzzle  # Import helper functions
from benchmark import compare_heuristics  # Import comparison logic
import Heuristic


def main():
    puzzle = Puzzle()
    display_board(puzzle)

    manhattan = Heuristic.ManhattanDistance(puzzle)
    manhattan_cost = manhattan.calculate(puzzle.gameBoard)
    print(f"Manhattan Distance: {manhattan_cost}")

    hamming = Heuristic.HammingDistance(puzzle)
    hamming_cost = hamming.calculate(puzzle.gameBoard)
    print(f"Hamming Distance: {hamming_cost}")

    if puzzle.isGoalReached():
        print("The Puzzle is already solved!")
        return

    print("The Goal State is not yet reached. Starting calculations...")
    solve_puzzle(puzzle, Heuristic.ManhattanDistance)

    choice = input("\nDo you want to perform a heuristic comparison? (yes/no): ").strip().lower()
    if choice == "yes":
        try:
            num_trials = int(input("Enter the number of random puzzles to compare: "))
            if num_trials > 0:
                compare_heuristics(num_trials)
            else:
                print("Invalid input. Exiting.")
        except ValueError:
            print("Invalid input. Exiting.")
    elif choice == "no":
        print("Heuristic comparison skipped. Exiting.")
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()