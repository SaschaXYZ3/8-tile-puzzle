from Puzzle import Puzzle  # Import the Puzzle class from the Puzzle module

class Nodes:
    def __init__(self, nodeId, parentId, heuristic, parentCost=0, gameBoard=None):
        """
        Initialize a Node object.
        """
        self.nodeId = nodeId  # Unique ID for the node
        self.parent = parentId  # Parent node ID
        self.puzzle = Puzzle(gameBoard)  # Create a Puzzle object with the gameboard
        self.heuristic = heuristic  # Heuristic used for cost calculation
        self.children = []  # List to store child node IDs
        # Calculate the cost using the heuristic function
        self.cost = heuristic.calculate(self.puzzle.gameBoard, parentCost)

    def addChild(self, childId):
        """
        Add a child node ID to the list of children.
        """
        self.children.append(childId)
