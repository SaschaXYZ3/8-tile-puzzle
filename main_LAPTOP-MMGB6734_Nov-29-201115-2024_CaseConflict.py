from puzzle import Puzzle
from heuristic import ManhattanDistance
from heuristic import HammingDistance
from queue import a_star

def main():
    # Generate a new puzzle
    myPuzzle = Puzzle()  
    
    # Drucke das generierte Spielfeld
    print("Generiertes Spielfeld:")
    myPuzzle.printGameBoard()

    # Prüfe, ob das Puzzle lösbar ist
    if myPuzzle.isSolvable():
        print("Das Puzzle ist lösbar!")
    else:
        print("Das Puzzle ist NICHT lösbar.")

    # Zusätzliche Informationen
    print("\nMisplaced Tiles Cost (Hamming):", myPuzzle.getMisplacedTilesCost())
    print("Manhattan Distance Cost:", myPuzzle.getManhattanCost())
    print("\nErreichtes Zielzustand?", myPuzzle.isGoalReached())

    manhattenHeuristic1 = ManhattanDistance(myPuzzle.goalState, costExponent=1)
    hammingHeuristic1= HammingDistance(myPuzzle.goalState, costExponent=1)
    manhattenHeuristic11= ManhattanDistance(myPuzzle.goalState, costExponent=11)
    hammingHeuristic11= HammingDistance(myPuzzle.goalState, costExponent=11)

    print("Manhattan Distance (Exponent 1):",
          manhattenHeuristic1.calculate(myPuzzle.gameBoard, parentCost=0))
    print("Hamming Distance (Exponent 1):",
          hammingHeuristic1.calculate(myPuzzle.gameBoard, parentCost=0))
    print("Manhattan Distance (Exponent 11):",
          manhattenHeuristic11.calculate(myPuzzle.gameBoard, parentCost=0))
    print("Hamming Distance (Exponent 11):",
          hammingHeuristic11.calculate(myPuzzle.gameBoard, parentCost=0))
    
    

# test A* Algorithm with one heuristic
    result = a_star(myPuzzle, Puzzle.getManhattanCost)
    print("Pfadkosten:", result["path_cost"])
    print("Expandierte Knoten:", result["nodes_expanded"])
    print("Lösung gefunden:", result["solution"])
    print("Laufzeit:", result["runtime"])


if __name__ == "__main__":
    main()