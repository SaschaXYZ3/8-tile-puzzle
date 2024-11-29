from Nodes import Nodes


# Umbenennung der Klasse in AStarQueue, um Konflikte zu vermeiden
class AStarQueue:

    def __init__(self, heuristicClass):
        # Initialisiere die Queue mit den notwendigen Attributen
        self.nodes = {}  # Wörterbuch zum Speichern von Knoten nach deren ID
        self.nextNodeId = 0  # ID für den nächsten Knoten
        self.openNodes = {}  # Knoten, die noch untersucht werden müssen
        self.path = []  # Der Lösungspfad als Liste von Knoten-IDs
        self.numberOfMoves = 0  # Anzahl der Schritte zur Lösung des Puzzles
        self.heuristicClass = heuristicClass  # Heuristik für das Puzzle

    def reset(self):
        # Setze die Queue in ihren Ausgangszustand zurück
        self.nodes = {}
        self.nextNodeId = 0
        self.openNodes = {}
        self.path = []

    def setFirstNode(self):
        # Erstelle den ersten Knoten und markiere ihn als offen
        self.nodes[self.nextNodeId] = Nodes(self.nextNodeId, None, self.heuristicClass, 0)
        self.openNodes[self.nextNodeId] = self.nodes[self.nextNodeId]
        self.nextNodeId += 1

    def findCheapestNode(self):
        # Finde den Knoten mit den niedrigsten Kosten in openNodes
        cheapestNode = None
        cheapestNodeId = None
        for nodeId, node in self.openNodes.items():
            if cheapestNode is None or node.cost < cheapestNode.cost:
                cheapestNode = node
                cheapestNodeId = nodeId
        return cheapestNodeId

    def addNode(self, parentId, gameBoard):
        # Füge einen neuen Knoten zum Baum hinzu und markiere ihn als offen
        parentNode = self.nodes[parentId]
        # Die Kosten vom Startknoten zu diesem neuen Knoten sind die Kosten des Elternknotens + 1
        newNode = Nodes(self.nextNodeId, parentId, self.heuristicClass, parentNode.gCost, gameBoard)
        self.nodes[self.nextNodeId] = newNode
        self.openNodes[self.nextNodeId] = newNode  # Markiere diesen Knoten als offen
        parentNode.addChild(self.nextNodeId)  # Füge diesen Knoten zu den Kindern des Elternknotens hinzu
        self.nextNodeId += 1

    def doesNodeExist(self, gameBoard):
        # Überprüfe, ob ein Knoten mit dem gleichen Spielbrett bereits existiert
        for nodeId, node in self.nodes.items():
            if node.puzzle.compareGameBoards(gameBoard):
                return True
        return False

    def expandNode(self, nodeId):
        # Erweitere einen Knoten, indem du seine möglichen Kinder erzeugst
        self.openNodes.pop(nodeId)
        parentNode = self.nodes[nodeId]
        for gameBoard in parentNode.puzzle.generatePossibleMoves():
            if not parentNode.puzzle.compareGameBoards(gameBoard):
                if not self.doesNodeExist(gameBoard):
                    self.addNode(nodeId, gameBoard)

    def getPath(self, nodeId):
        # Verfolge den Pfad von einem Knoten bis zum Wurzelknoten
        path = []
        while nodeId is not None:
            path.append(nodeId)
            nodeId = self.nodes[nodeId].parent
        self.numberOfMoves = len(path) - 1
        return path[::-1]  # Umkehren des Pfades

    def printPath(self):
        # Gib den Lösungspfad aus, dabei werden die Änderungen hervorgehoben
        previousGameBoard = None

        for nodeId in self.path:
            currentGameBoard = self.nodes[nodeId].puzzle.gameBoard

            if previousGameBoard is not None:
                print()
                for i in range(len(currentGameBoard)):
                    for j in range(len(currentGameBoard[i])):
                        if currentGameBoard[i][j] != previousGameBoard[i][j]:
                            print("\033[31m{}\033[00m".format(currentGameBoard[i][j]), end=' ')
                        else:
                            print(currentGameBoard[i][j], end=' ')
                    print()
            else:
                for row in currentGameBoard:
                    print(' '.join(map(str, row)))

            previousGameBoard = currentGameBoard

    def findSolution(self):
        # Finde die Lösung des Puzzles unter Verwendung des heuristischen Suchalgorithmus
        self.reset()
        self.setFirstNode()
        cheapestNodeId = 0
        run = 0

        while True:
            run += 1
            if cheapestNodeId is None:
                return None
            if self.nodes[cheapestNodeId].puzzle.isGoalReached():
                self.path = self.getPath(cheapestNodeId)
                return None
            self.expandNode(cheapestNodeId)
            cheapestNodeId = self.findCheapestNode()

"""
            print(
                f"Current node: {cheapestNodeId}, Cost: {self.nodes[cheapestNodeId].cost}, "
                f"Parent: {self.nodes[cheapestNodeId].parent}, Run: {run}, "
                f"Current Cost: {self.nodes[cheapestNodeId].puzzle.getCost()}, "
                f"Open Nodes: {len(self.openNodes)}"
            )
"""
"""
# A* Algorithm number of nodes expanded
def a_star(puzzle, heuristic):
    start_time = time.time()   # start timer
    open_list = []            # Priority Queue for the minimum f(n)-value
    closed_list = set()       # for expanded nodes
    heapq.heappush(open_list, (0, puzzle.gameBoard, 0))   # f_cost, board, g_cost
    nodes_expanded = 0        # count for expanded nodes

    while open_list:    # take the node with the minimum f_cost
        f_cost, current_board, g_cost = heapq.heappop(open_list)
        current_puzzle = Puzzle(current_board)

        #print(f"Open list memory: {open_list_memory} bytes")
        #print(f"Closed list memory: {closed_list_memory} bytes")

        if current_puzzle.isGoalReached(): # check if goal is reached
            end_time = time.time()  # end timer
            runtime = end_time -start_time # calculate runtime
            # calculate storage of both lists
            open_list_memory = sum(sys.getsizeof(item) for item in open_list)
            closed_list_memory = sum(sys.getsizeof(item) for item in closed_list)
            memory_usage = open_list_memory + closed_list_memory
            return {
                "path_cost": g_cost,
                "nodes_expanded": nodes_expanded,
                "solution": current_board,
                 "runtime": runtime,
                "memory_usage": memory_usage / (1024 ** 2),  # memory in MB
            }
         # add actuall state to closed_list
        closed_list.add(tuple(map(tuple,current_board)))

        # generate neighbors and check
        for neighbor in current_puzzle.generatePossibleMoves():
            neighbor_tuple = tuple(map(tuple,neighbor))
            if neighbor_tuple in closed_list:
                continue    # continue already achieved states

            # calculate g,h and f for neighbor
            g_neighbor = g_cost + 1         # every movement costs 1
            h_neighbor = heuristic(Puzzle(neighbor))
            f_neighbor = g_neighbor + h_neighbor

            # put neighbours into the open_list
            heapq.heappush(open_list, (f_neighbor, neighbor, g_neighbor))
            nodes_expanded += 1
            """