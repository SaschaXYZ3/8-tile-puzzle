from AStarQueue import AStarQueue
from Puzzle import Puzzle
import Heuristic
import time
import threading


def main():
    # Create a puzzle object
    puzzle = Puzzle()  # A random but solvable game board is created here

    # Show the current puzzle
    print("Current Puzzle (Gameboard):")
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
        print("The Puzzle is already solved!")
    else:
        print("The Goal is not yet reached. Starting calculations...")

        # Run A* algorithm to solve the puzzle
        # We can use the Manhattan distance or the Hamming distance as a heuristic here
        heuristic = Heuristic.ManhattanDistance(puzzle)  # Select the heuristic (Manhattan or Hamming)
        queue = AStarQueue(heuristic)  # Initialize the AStarQueue (A* algorithm)

        # Find the solution to the puzzle
        start_time = time.time()
        queue.findSolution()
        end_time = time.time()

        # Output of the solution path
        print("\nSolution path:")
        queue.printPath()

        # Show the number of steps needed to solve the puzzle
        print(f"Number of Moves required: {queue.numberOfMoves}")

        # Output the runtime
        print(f"Runtime: {end_time - start_time} Seconds")


    # Compare heuristics
    """ 
    Manhattan is waaaaay more effective than Hamming.
    Consider calculation times up to several minutes!!!!!!
    With A*, the number of nodes expanded increases exponentially with the depth of the solution when the heuristic is less informative.
    ToDo eventually: limit max number of expanded nodes or iterations
    """

    # Ask the user if they want to perform heuristic comparison
    print("\nDo you want to perform a heuristic comparison?")
    choice = input("Enter 'yes' to proceed or 'no' to skip: ").strip().lower()

    if choice == "yes":
        try:
            num_trials = int(input("Enter the number of random puzzles to compare: "))
            if num_trials <= 0:
                print("The number of puzzles must be greater than 0. Exiting.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number. Exiting.")
            return

        # Run the comparison
        print(f"\nStarting heuristic comparison of {num_trials} puzzles")
        compare_heuristics(num_trials=num_trials)
    elif choice == "no":
        print("Heuristic comparison skipped. Exiting program.")
    else:
        print("Invalid choice. Exiting program.")


def compare_heuristics_timed(num_trials):
    """
    Compare Manhattan and Hamming heuristics over multiple random puzzles.

    Parameters:
    - num_trials: Number of random puzzles to test.

    Outputs:
    - Average time taken by each heuristic
    - Average number of expanded nodes for each heuristic
    """
    manhattan_results = {"time": 0, "expanded_nodes": 0}
    hamming_results = {"time": 0, "expanded_nodes": 0}
    start_time = time.time()

    # Timer thread to log elapsed time every second
    def log_timer():
        while not stop_timer.is_set():
            elapsed = int(time.time() - start_time)
            print(f"Elapsed time: {elapsed} seconds")
            time.sleep(10)

    # Start the timer thread
    stop_timer = threading.Event()
    timer_thread = threading.Thread(target=log_timer)
    timer_thread.start()

    try:
        for trial in range(num_trials):
            print(f"Trial {trial + 1} of {num_trials}...")  # Progress indicator
            puzzle = Puzzle()  # Generate a random solvable puzzle

            # Run comparison for each heuristic
            for heuristic_name, heuristic_class, results in [
                ("Manhattan", Heuristic.ManhattanDistance, manhattan_results),
                ("Hamming", Heuristic.HammingDistance, hamming_results),
            ]:
                heuristic = heuristic_class(puzzle)
                queue = AStarQueue(heuristic)

                # Measure time
                heuristic_start = time.time()
                queue.findSolution()
                heuristic_end = time.time()

                # Record results
                results["time"] += heuristic_end - heuristic_start
                results["expanded_nodes"] += len(queue.nodes)

    finally:
        # Stop the timer thread
        stop_timer.set()
        timer_thread.join()

    # Print results
    print("\nComparison of Heuristics:")
    print(f"Manhattan: Avg Time: {manhattan_results['time'] / num_trials:.4f}s, "
          f"Avg Expanded Nodes: {manhattan_results['expanded_nodes'] / num_trials}")
    print(f"Hamming: Avg Time: {hamming_results['time'] / num_trials:.4f}s, "
          f"Avg Expanded Nodes: {hamming_results['expanded_nodes'] / num_trials}")

def compare_heuristics(num_trials):
    """
    Compare Manhattan and Hamming heuristics over multiple random puzzles.

    Parameters:
    - num_trials: Number of random puzzles to test.

    Outputs:
    - Average time taken by each heuristic
    - Average number of expanded nodes for each heuristic
    """
    manhattan_results = {"time": 0, "expanded_nodes": 0}
    hamming_results = {"time": 0, "expanded_nodes": 0}

    for trial in range(num_trials):
        print(f"--- Trial {trial + 1} of {num_trials} ---")  # Mark start of each trial
        retries = 0

        while True:  # Keep generating puzzles until a solvable one is found
            retries += 1
            puzzle = Puzzle()

            if puzzle.isSolvable(puzzle.gameBoard):
                print(f"Generated a solvable board after {retries} retries:")
                puzzle.printGameBoard()
                break  # Exit loop if solvable

            print("Generated unsolvable board, retrying...")

        # Run comparison for each heuristic
        for heuristic_name, heuristic_class, results in [
            ("Manhattan", Heuristic.ManhattanDistance, manhattan_results),
            ("Hamming", Heuristic.HammingDistance, hamming_results),
        ]:
            heuristic = heuristic_class(puzzle)
            queue = AStarQueue(heuristic)

            # Measure time
            start_time = time.time()
            queue.findSolution()
            end_time = time.time()

            # Record results
            results["time"] += end_time - start_time
            results["expanded_nodes"] += len(queue.nodes)

    # Print results
    print("\nComparison of Heuristics:")
    print(f"Manhattan: Avg Time: {manhattan_results['time'] / num_trials:.4f}s, "
          f"Avg Expanded Nodes: {manhattan_results['expanded_nodes'] / num_trials}")
    print(f"Hamming: Avg Time: {hamming_results['time'] / num_trials:.4f}s, "
          f"Avg Expanded Nodes: {hamming_results['expanded_nodes'] / num_trials}")

if __name__ == "__main__":
    main()

