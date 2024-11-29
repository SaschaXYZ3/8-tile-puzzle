import Queue
from Puzzle import Puzzle
import Heuristic
import time

def main():
    """# Generate a new puzzle
    myPuzzle = Puzzle()  
    
    # Drucke das generierte Spielfeld
    print("Generiertes Spielfeld:")
    myPuzzle.printGameBoard()

    # Prüfe, ob das Puzzle lösbar ist
    if myPuzzle.isSolvable():
        print("Das Puzzle ist lösbar!")
    else:
        print("Das Puzzle ist NICHT lösbar.")
    """
    # Erstelle verschiedene Test-Queues mit unterschiedlichen Heuristiken
    queueArray = [
        Queue(Heuristic.manhattanDistance(Puzzle.goalState, 1)),
        Queue(Heuristic.hammingDistance(Puzzle.goalState, 1)),
        Queue(Heuristic.manhattanDistance(Puzzle.goalState, 11)),
        Queue(Heuristic.hammingDistance(Puzzle.goalState, 11))
    ]

    # Liste zur Speicherung der Laufzeiten
    executionTimes = []

    # Führe Tests für jede Queue aus
    for xQueue in queueArray:
        startTime = time.time()  # Startzeit messen
        xQueue.findSolution()  # Lösung finden
        print("----------------------------")
        executionTimes.append(time.time() - startTime)  # Laufzeit speichern

    # Ergebnisse ausgeben
    for i in range(len(executionTimes)):
        heuristicName = queueArray[i].heuristicClass.__class__.__name__
        timeTaken = executionTimes[i]
        moves = queueArray[i].numberOfMoves
        print(f"Time for solution with {heuristicName} heuristic: {timeTaken:.2f} seconds, Number of moves: {moves}")
    
    """
    # Zusätzliche Informationen
    print("\nMisplaced Tiles Cost (Hamming):", myPuzzle.getMisplacedTilesCost())
    print("Manhattan Distance Cost:", myPuzzle.getManhattanCost())
    print("\nErreichtes Zielzustand?", myPuzzle.isGoalReached())
    """
    """
    queue1 = Queue(Heuristic.ManhattanDistance(Puzzle.goalState,1))
    queue2 = Queue(Heuristic.HammingDistance(Puzzle.goalState,1))
    queue3 = Queue(Heuristic.ManhattanDistance(Puzzle.goalState,11))
    queue4 = Queue(Heuristic.HammingDistance(Puzzle.goalState,11))

    startTime1 = time.time()
    queue1.findSolution()
    endTime1 = time.time()
    
    runTime = endTime1 - startTime1
    print("first Queue: " + runTime)
    
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
    """

if __name__ == "__main__":
    main()