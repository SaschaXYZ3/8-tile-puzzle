from AStarQueue import AStarQueue
from Puzzle import Puzzle
import Heuristic
import time


def compare_heuristics(num_trials):
    """
    Compare Manhattan and Hamming heuristics over multiple random puzzles.

    Args:
        num_trials (int): Number of puzzles to compare.

    Prints:
        Average time and number of expanded nodes for each heuristic.
    """
    from Heuristic import ManhattanDistance, HammingDistance
    import time

    results = {"Manhattan": {"time": 0, "nodes": 0}, "Hamming": {"time": 0, "nodes": 0}}

    for trial in range(num_trials):
        print(f"Trial {trial + 1} of {num_trials}...")

        # Generate a random solvable puzzle
        puzzle = Puzzle()

        for heuristic_name, heuristic_class in [("Manhattan", ManhattanDistance), ("Hamming", HammingDistance)]:
            print(f"\nUsing {heuristic_name} Heuristic:")

            # Create a heuristic instance
            heuristic_instance = heuristic_class(puzzle)

            # Pass puzzle and heuristic to AStarQueue
            queue = AStarQueue(puzzle, heuristic_instance)

            # Measure time
            start_time = time.time()
            queue.findSolution()
            end_time = time.time()

            # Record results
            results[heuristic_name]["time"] += (end_time - start_time)
            results[heuristic_name]["nodes"] += len(queue.nodes)

    # Display results
    print("\nComparison of Heuristics:")
    for heuristic_name in results:
        avg_time = results[heuristic_name]["time"] / num_trials
        avg_nodes = results[heuristic_name]["nodes"] / num_trials
        print(f"{heuristic_name}: Avg Time: {avg_time:.4f}s, Avg Expanded Nodes: {avg_nodes:.1f}")