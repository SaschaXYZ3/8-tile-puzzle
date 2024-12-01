from Nodes import Nodes
import heapq

# Rename the class to AStarQueue to avoid conflicts
class AStarQueue:

    def __init__(self, heuristicClass):
        self.nodes = {}  # Dictionary for saving nodes according to their ID
        self.nextNodeId = 0  # ID for the next node
        self.openNodes = []  # Priority queue for open nodes (heapq)
        self.path = []  # The solution path as a list of node IDs
        self.numberOfMoves = 0  # Number of steps to solve the puzzle
        self.heuristicClass = heuristicClass  # Heuristics for the puzzle
        self.nodeStates = set()  # Set to store unique game board states

    def reset(self):
        # Reset the queue to its initial state
        self.nodes = {}
        self.nextNodeId = 0
        self.openNodes = []
        self.path = []

    def setFirstNode(self):
        firstNode = Nodes(self.nextNodeId, None, self.heuristicClass, 0)
        self.nodes[self.nextNodeId] = firstNode

        # Debugging check
        if not isinstance(self.openNodes, list):
            raise TypeError("openNodes must be a list for heapq operations.")

        heapq.heappush(self.openNodes, (firstNode.cost, self.nextNodeId))
        self.nextNodeId += 1

    def findCheapestNode(self):
        """Find and return the ID of the cheapest node in the openNodes queue."""
        if not self.openNodes:
            return None  # No nodes left to process
        return heapq.heappop(self.openNodes)[1]  # Pop and return the node ID

    def addNode(self, parentId, gameBoard):
        parentNode = self.nodes[parentId]
        newNode = Nodes(self.nextNodeId, parentId, self.heuristicClass, parentNode.gCost, gameBoard)
        self.nodes[self.nextNodeId] = newNode
        heapq.heappush(self.openNodes, (newNode.cost, self.nextNodeId))  # Add to priority queue
        parentNode.addChild(self.nextNodeId)  # Link to parent
        self.nodeStates.add(tuple(map(tuple, gameBoard)))  # Track the state
        self.nextNodeId += 1

    def doesNodeExist(self, gameBoard):
        """Check whether a node with the same board already exists."""
        return tuple(map(tuple, gameBoard)) in self.nodeStates

    def expandNode(self, nodeId):
        """Expand a node by generating its possible children."""
        parentNode = self.nodes[nodeId]
        for gameBoard in parentNode.puzzle.generatePossibleMoves():
            if not self.doesNodeExist(gameBoard):  # Check for duplicates
                self.addNode(nodeId, gameBoard)
        # Remove the node from the open list (already processed)
        self.openNodes = [node for node in self.openNodes if node[1] != nodeId]
        heapq.heapify(self.openNodes)  # Re-heapify after removal

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

    def findSolution(self, max_iterations=20000, max_nodes=25000):
        """
        Find the solution to the puzzle using the heuristic search algorithm.

        Args:
            max_iterations (int): Maximum number of iterations before terminating.
            max_nodes (int): Maximum number of nodes to expand before terminating.

        Returns:
            None
        """
        self.reset()
        self.setFirstNode()
        run = 0
        total_expanded_nodes = 0
        max_iterations_count = 0
        max_expansion_count = 0

        while self.openNodes:
            run += 1

            # Get the cheapest node
            cheapestNodeId = self.findCheapestNode()
            if cheapestNodeId is None:
                print("No solution found.")
                return None

            current_node = self.nodes[cheapestNodeId]

            # Check if the goal state is reached
            if current_node.puzzle.isGoalReached():
                print(f"Solution found after {run} iterations.")
                self.path = self.getPath(cheapestNodeId)
                return  # Exit the loop and method

            # Termination condition: check iteration limit
            if run > max_iterations:
                max_iterations_count += 1
                print(f"Terminated: Maximum iterations ({max_iterations}) reached. Violating iterations count: {max_iterations_count}")
                return None

            # Expand the current node
            self.expandNode(cheapestNodeId)
            total_expanded_nodes += 1

            # Termination condition: check expanded nodes limit
            if total_expanded_nodes > max_nodes:
                max_expansion_count += 1
                print(f"Terminated: Maximum expanded nodes ({max_nodes}) reached. Violating Nodes count: {max_expansion_count}")
                return None

            # Optional debugging output
            #if run % 100 == 0:  # Print every 100 iterations
            #    print(f"Iteration: {run}, Open Nodes: {len(self.openNodes)}, "
            #          f"Expanded Nodes: {total_expanded_nodes}")
