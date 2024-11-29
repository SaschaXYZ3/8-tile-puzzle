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

        # A*-Algorithmus ausführen, um das Puzzle zu lösen
        # Wir können hier die Manhattan-Distanz oder die Hamming-Distanz als Heuristik verwenden
        heuristic = Heuristic.ManhattanDistance(puzzle)  # Wähle die Heuristik (Manhattan oder Hamming)
        queue = AStarQueue(heuristic)  # Initialisiere die AStarQueue (A*-Algorithmus)

        # Finde die Lösung des Puzzles
        start_time = time.time()
        queue.findSolution()
        end_time = time.time()

        # Ausgabe des Lösungspfads
        print("\nLösungspfad:")
        queue.printPath()

        # Zeige die Anzahl der Schritte, die benötigt wurden, um das Puzzle zu lösen
        print(f"Anzahl der Schritte: {queue.numberOfMoves}")

        # Gib die Laufzeit aus
        print(f"Berechnungszeit: {end_time - start_time} Sekunden")


if __name__ == "__main__":
    main()