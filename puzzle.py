import random

class puzzle:
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
        """Create a random gameboard that is solvable."""
        # Creating 3x3 array for the gameboard
        self.gameBoard = [[0] * 3 for _ in range(3)]
        # Shuffle numbers until solvable
        isSolvable = False

        while not isSolvable:

            self.numbers = [1,2,3,4,5,6,7,0,8]
            random.shuffle(self.numbers)
            for i in range(3):
                for j in range(3):
                    # Pop first number from shuffled list and assign it to gameboard
                    self.gameBoard[i][j] = self.numbers.pop(0)

            # Check if puzzle is solvable
            isSolvable = self.isSolvable()

    def printGameBoard(self):
        """Print the current state of the gameboard in a readable format."""
        for row in self.gameBoard:
            print(row)
 
    def isSolvable(self):
        """Check if the puzzle is solvable based on the number of inversions."""
        inversions = 0
        flattenedPuzzle = []
        for row in self.gameBoard:  # Loop through each row in the gameboard
            for tile in row:  # Loop through each tile in the row
                if tile != 0:  # Check if the tile is not 0
                    flattenedPuzzle.append(tile)  # Add the tile to the flattened_puzzle list

        for i in range(len(flattenedPuzzle)):
            for j in range(i + 1, len(flattenedPuzzle)):
                if flattenedPuzzle[i] > flattenedPuzzle[j]:
                    inversions += 1

        # Check if even number
        if len(self.gameBoard) % 2 != 0:
            return inversions % 2 == 0
        else:
            blank_row = next(row for row, tiles in enumerate(self.gameBoard)
                             if 0 in tiles)
            return (blank_row % 2 == 0) == (inversions % 2 != 0)

    def isGoalReached(self):
        """Check if the current gameboard matches the goal state."""
        return self.gameBoard == puzzle.goalState
    
    def getMisplacedTilesCost(self):
        """Calculate the cost based on the number of misplaced tiles."""
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.gameBoard[i][j] != 0 and self.gameBoard[i][j] != puzzle.goalState[i][j]:
                    cost += 1
        return cost

    def getManhattanCost(self):
        """Calculate the cost based on the Manhattan distance."""
        cost = 0
        for i in range(3):
            for j in range(3):
                tile = self.gameBoard[i][j]
                if tile != 0:
                    # Find the correct position of the tile in the goal state
                    targetRow = tile // 3
                    targetCol = tile % 3
                    # Calculate the Manhattan distance
                    cost += abs(i - targetRow) + abs(j - targetCol)
        return cost

    def copyGameBoard(self):
        """Create a copy of the current gameboard."""
        return [row[:] for row in self.gameBoard]

    def getEmptyPosition(self):
        """Find the row and column of the empty tile (0)."""
        for i, row in enumerate(self.gameBoard):
            for j, tile in enumerate(row):
                if tile == 0:
                    return i, j

    def generatePossibleMoves(self):
        """Generate all possible gameboards after moving the empty tile."""
        emptyRow, emptyCol = self.getEmptyPosition()
        possibleGameBoards = []

        # Check if moving the blank tile up is possible
        if emptyRow > 0:
            newGameBoard = self.copyGameBoard()
            newGameBoard[emptyRow][emptyCol], newGameBoard[emptyRow - 1][emptyCol] = \
                newGameBoard[emptyRow - 1][emptyCol], newGameBoard[emptyRow][emptyCol]
            possibleGameBoards.append(newGameBoard)

        # Check if moving the blank tile down is possible
        if emptyRow < 2:
            newGameBoard = self.copyGameBoard()
            newGameBoard[emptyRow][emptyCol], newGameBoard[emptyRow + 1][emptyCol] = \
                newGameBoard[emptyRow + 1][emptyCol], newGameBoard[emptyRow][emptyCol]
            possibleGameBoards.append(newGameBoard)

        # Check if moving the blank tile left is possible
        if emptyCol > 0:
            newGameBoard = self.copyGameBoard()
            newGameBoard[emptyRow][emptyCol], newGameBoard[emptyRow][emptyCol - 1] = \
                newGameBoard[emptyRow][emptyCol - 1], newGameBoard[emptyRow][emptyCol]
            possibleGameBoards.append(newGameBoard)

        # Check if moving the blank tile right is possible
        if emptyCol < 2:
            newGameBoard = self.copyGameBoard()
            newGameBoard[emptyRow][emptyCol], newGameBoard[emptyRow][emptyCol + 1] = \
                newGameBoard[emptyRow][emptyCol + 1], newGameBoard[emptyRow][emptyCol]
            possibleGameBoards.append(newGameBoard)

        return possibleGameBoards
