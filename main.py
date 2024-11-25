from puzzle import puzzle

def main():
    # Generate a new puzzle
    myPuzzle = puzzle()  
    
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

if __name__ == "__main__":
    main()