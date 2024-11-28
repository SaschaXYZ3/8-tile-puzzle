class ManhattanDistance:
    def __init__(self, goalState, costExponent=3):
        """
        Initialize the ManhattanDistance heuristic.

        Parameters:
        - goalState: The target configuration of the puzzle.
        - costExponent: A multiplier to scale the cost (default is 3).
        """
        self.goalState = goalState
        self.costExponent = costExponent

    def calculate(self, gameBoard, parentCost):
        """
        Calculate the Manhattan distance cost for the given gameBoard.

        Parameters:
        - gameBoard: The current puzzle configuration.
        - parentCost: The accumulated cost from the parent node.

        Returns:
        - Total cost (Manhattan distance raised to the power of costExponent plus parent cost).
        """
        cost = 0
        # Compare each tile in the gameBoard to its position in the goal state
        for i in range(3):  # Loop through rows
            for j in range(3):  # Loop through columns
                if gameBoard[i][j] != self.goalState[i][j] and gameBoard[i][j] != 0:  # Ignore blank tile
                    # Find the correct position of the current tile in the goal state
                    targetRow = (gameBoard[i][j] - 1) // 3
                    targetCol = (gameBoard[i][j] - 1) % 3
                    # Add the Manhattan distance (row and column differences)
                    cost += abs(i - targetRow) + abs(j - targetCol)
        # Apply the cost exponent and add the parent cost
        return cost ** self.costExponent + parentCost


class HammingDistance:
    def __init__(self, goalState, costExponent=3):
        """
        Initialize the HammingDistance heuristic.

        Parameters:
        - goalState: The target configuration of the puzzle.
        - costExponent: A multiplier to scale the cost (default is 3).
        """
        self.goalState = goalState
        self.costExponent = costExponent

    def calculate(self, gameBoard, parentCost):
        """
        Calculate the Hamming distance cost for the given gameBoard.

        Parameters:
        - gameBoard: The current puzzle configuration.
        - parentCost: The accumulated cost from the parent node.

        Returns:
        - Total cost (Hamming distance raised to the power of costExponent plus parent cost).
        """
        cost = 0
        # Compare each tile in the gameBoard to its position in the goal state
        for i in range(3):  # Loop through rows
            for j in range(3):  # Loop through columns
                if gameBoard[i][j] != self.goalState[i][j] and gameBoard[i][j] != 0:  # Ignore blank tile
                    # Find the correct position of the current tile in the goal state
                    for k in range(3):  # Loop through goal rows
                        for l in range(3):  # Loop through goal columns
                            if gameBoard[i][j] == self.goalState[k][l]:
                                # Add the Manhattan distance (row and column differences)
                                cost += abs(i - k) + abs(j - l)
        # Apply the cost exponent and add the parent cost
        return cost ** self.costExponent + parentCost
