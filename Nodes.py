from Puzzle import Puzzle  # Import the Puzzle class from the Puzzle module

class Nodes:
    def __init__(self, nodeId, parentId, heuristic, parentCost=0, gameBoard=None):
        """
        Initialize a Node object.

        Args:
            nodeId (int): Unique ID of the node.
            parentId (int): ID of the parent node.
            heuristic (object): The heuristic object to calculate costs.
            parentCost (int): Cost from the start to the parent node.
            gameBoard (list of list): The puzzle's game board.
        """
        self.nodeId = nodeId  # Unique ID
        self.parent = parentId  # Parent node ID
        self.puzzle = Puzzle(gameBoard)  # Create a Puzzle object with the board
        self.heuristic = heuristic  # Heuristic used for cost calculation
        self.children = []  # List of child node IDs

        # Calculate costs
        self.gCost = parentCost + 1  # Cost from start to this node
        self.hCost = self.heuristic.calculate(self.puzzle.gameBoard)  # Heuristic cost
        self.cost = self.gCost + self.hCost  # Total cost (f = g + h)

    def addChild(self, childId):
        """
        Add a child node ID to the list of children.
        """
        self.children.append(childId)

    def __repr__(self):
        """
        String-Darstellung für Debugging-Zwecke.
        """
        return f"Node {self.nodeId} (g: {self.gCost}, h: {self.hCost}, f: {self.cost})"
