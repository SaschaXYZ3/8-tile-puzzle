import random

class Puzzle:

    # define goalstate
    goalState = [[0, 1, 2],
                 [3, 4, 5],
                 [6, 7, 8]]  # 0 is blank tile on top left

    def __init__(self, gameBoard=None):
        """Initialize the puzzle with a gameboard. If no gameboard is provided, create one."""
        self.gameBoard = gameBoard
        if self.gameBoard is None:
            self.createRandomGameBoard()

    def createRandomGameBoard(self):
        """Create and return a random solvable game board."""
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        while True:
            random.shuffle(numbers)
            self.gameBoard = [numbers[i:i + 3] for i in range(0, len(numbers), 3)]
            if self.isSolvable(self.gameBoard):
                return self.gameBoard

            # Debug: Check the flat list and inversion count
            #flat = [tile for row in self.gameBoard for tile in row]
            #print(f"Generated flat board: {flat}")

    @staticmethod
    def isSolvable(gameBoard):
        """
        Check if a given puzzle board is solvable based solely on the inversion count.

        Args:
            gameBoard (list of list of int): The 3x3 puzzle board.

        Returns:
            bool: True if solvable, False otherwise.
        """
        # Flatten the board and remove the blank tile (0)
        flat = [tile for row in gameBoard for tile in row if tile != 0]

        # Count inversions
        inversions = sum(
            1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] > flat[j]
        )

        # Solvable if the inversion count is even
        return inversions % 2 == 0

    def isGoalReached(self):
        """Check if the current gameboard matches the goal state."""
        if self.gameBoard == Puzzle.goalState:
            return True
        else:
            return False

    def copyGameBoard(self):
        """Create a copy of the current gameboard."""
        return [
            row[:] for row in self.gameBoard
        ]

    def getEmptyPosition(self):
        """Find the row and column of the empty tile (0)."""
        for i, row in enumerate(self.gameBoard):
            for j, tile in enumerate(row):
                if tile == 0:
                    return i, j

    def generatePossibleMoves(self):
        """Generate all possible gameboards after moving the empty tile."""
        neighbors = []

        # find the position with the blank space
        emptyRow, emptyCol = self.getEmptyPosition()

        # possible movements
        moves = [
            (-1, 0),   # up
            (1, 0),   # down
            (0, -1),   # left
            (0, 1)    # right
        ]

        for moveRow, moveCol in moves:
            newRow = emptyRow + moveRow
            newCol = emptyCol + moveCol

            if 0 <= newRow < 3 and 0 <= newCol < 3:  # check if the movements are in 3x3
                newGameBoard = self.copyGameBoard()

                # switch the blank position with the target position
                newGameBoard[emptyRow][emptyCol], newGameBoard[newRow][newCol] = \
                    newGameBoard[newRow][newCol], newGameBoard[emptyRow][emptyCol]

                # add the new gameboard to the neighbour list
                neighbors.append(newGameBoard)

        return neighbors

    def compareGameBoards(self, otherGameBoard):
        """Compare actual gameboard with other one"""
        return self.gameBoard == otherGameBoard

    def printGameBoard(self):
        """Print the current state of the gameboard in a readable format."""
        for row in self.gameBoard:
            print(row)

    def getCost(self):
        """Calculate costs of actual state with Manhatten distance"""
        cost = 0
        for i in range(3):
            for j in range(3):
                tile = self.gameBoard[i][j]
                if tile != 0:  # Only for non-empty tiles
                    # Find the target position of the tile
                    targetRow = tile // 3
                    targetCol = tile % 3
                    # Calculate Manhattan distance
                    cost += abs(i - targetRow) + abs(j - targetCol)
        return cost