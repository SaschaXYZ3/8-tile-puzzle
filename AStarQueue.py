from Nodes import Nodes


# Rename the class to AStarQueue to avoid conflicts
class AStarQueue:

    def __init__(self, heuristicClass):
        # Initialize the queue with the necessary attributes
        self.nodes = {}  # Dictionary for saving nodes according to their ID
        self.nextNodeId = 0  # ID for the next node
        self.openNodes = {}  # Nodes that still need to be examined
        self.path = []  # The solution path as a list of node IDs
        self.numberOfMoves = 0  # Number of steps to solve the puzzle
        self.heuristicClass = heuristicClass  # Heuristics for the puzzle

    def reset(self):
        # Reset the queue to its initial state
        self.nodes = {}
        self.nextNodeId = 0
        self.openNodes = {}
        self.path = []

    def setFirstNode(self):
        # Create the first node and mark it as open
        self.nodes[self.nextNodeId] = Nodes(self.nextNodeId, None, self.heuristicClass, 0)
        self.openNodes[self.nextNodeId] = self.nodes[self.nextNodeId]
        self.nextNodeId += 1

    def findCheapestNode(self):
        # Find the node with the lowest cost in openNodes
        cheapestNode = None
        cheapestNodeId = None
        for nodeId, node in self.openNodes.items():
            if cheapestNode is None or node.cost < cheapestNode.cost:
                cheapestNode = node
                cheapestNodeId = nodeId
        return cheapestNodeId

    def addNode(self, parentId, gameBoard):
        # Add a new node to the tree and mark it as open
        parentNode = self.nodes[parentId]
        # The cost from the start node to this new node is the cost of the parent node + 1
        newNode = Nodes(self.nextNodeId, parentId, self.heuristicClass, parentNode.gCost, gameBoard)
        self.nodes[self.nextNodeId] = newNode
        self.openNodes[self.nextNodeId] = newNode  # Mark this node as open
        parentNode.addChild(self.nextNodeId)  # Add this node to the children of the parent node
        self.nextNodeId += 1

    def doesNodeExist(self, gameBoard):
        # Check whether a node with the same board already exists
        for nodeId, node in self.nodes.items():
            if node.puzzle.compareGameBoards(gameBoard):
                return True
        return False

    def expandNode(self, nodeId):
        # Expand a node by creating its possible children
        self.openNodes.pop(nodeId)
        parentNode = self.nodes[nodeId]
        for gameBoard in parentNode.puzzle.generatePossibleMoves():
            if not parentNode.puzzle.compareGameBoards(gameBoard):
                if not self.doesNodeExist(gameBoard):
                    self.addNode(nodeId, gameBoard)

    def getPath(self, nodeId):
        # Trace the path from a node to the root node
        path = []
        while nodeId is not None:
            path.append(nodeId)
            nodeId = self.nodes[nodeId].parent
        self.numberOfMoves = len(path) - 1
        return path[::-1]  # Reversing the path

    def printPath(self):
        # Enter the solution path, highlighting the changes
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
        # Find the solution to the puzzle using the heuristic search algorithm
        self.reset()
        self.setFirstNode()
        cheapestNodeId = 0
        run = 0

        while True:
            run += 1
            if cheapestNodeId is None:
                print("No solution found. Exiting.")
                return None
            current_node = self.nodes[cheapestNodeId]

            if current_node.puzzle.isGoalReached():
                print(f"A solution for the Puzzle was found after {run} iterations.")
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