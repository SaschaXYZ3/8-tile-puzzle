from puzzle import Puzzle, a_star

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

# test A* Algorithm with one heuristic
    result = a_star(myPuzzle, Puzzle.getManhattanCost)
    print("Pfadkosten:", result["path_cost"])
    print("Expandierte Knoten:", result["nodes_expanded"])
    print("Lösung gefunden:", result["solution"])


if __name__ == "__main__":
    main()