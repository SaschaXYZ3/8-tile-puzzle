from Puzzle import Puzzle  # Import the Puzzle class from the Puzzle module

class Nodes:
    def __init__(self, nodeId, parentId, heuristic, parentCost=0, gameBoard=None):
        """
        Initialize a Node object.
        """
        self.nodeId = nodeId  # Eindeutige ID für den Knoten
        self.parent = parentId  # Parent node ID
        self.puzzle = Puzzle(gameBoard)  # Erstellen Sie ein Puzzle-Objekt mit dem Spielbrett
        self.heuristic = heuristic  # Heuristic used for cost calculation
        self.children = []  # Liste zum Speichern der IDs untergeordneter Knoten

        # Calculate the cost using the heuristic function
        self.gCost = parentCost + 1  # Costs from parent node to this node
        self.hCost = self.heuristic.calculate(self.puzzle.gameBoard)  # Heuristics to the target
        self.cost = self.gCost + self.hCost  # G Overall rating (f = g + h)

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
