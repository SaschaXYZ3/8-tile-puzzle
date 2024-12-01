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

            # Debug: Check the flat list and inversion count
            flat = [tile for row in self.gameBoard for tile in row]
            print(f"Generated flat board: {flat}")

            if self.isSolvable(self.gameBoard):
                print("Generated solvable board:")
                for row in self.gameBoard:
                    print(row)
                return self.gameBoard
            else:
                print("Generated unsolvable board, retrying...")

    @staticmethod
    def isSolvable(gameBoard):
        """Check if the puzzle is solvable based on the number of inversions and blank tile position."""
        flat = [tile for row in gameBoard for tile in row if tile != 0]

        # Count inversions
        inversions = sum(
            1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] > flat[j]
        )

        # Find the row of the blank tile (0), counted from the bottom (1-indexed)
        blank_row_from_bottom = 3 - next(
            i for i, row in enumerate(gameBoard) if 0 in row
        )

        # Debug: Log inversion count and blank tile position
        print(f"Inversions: {inversions}, Blank Row (from bottom): {blank_row_from_bottom}")

        # Solvability check
        is_solvable = (inversions % 2 == 0 and blank_row_from_bottom % 2 == 1) or (
                inversions % 2 == 1 and blank_row_from_bottom % 2 == 0
        )

        # Debug: Log solvability result
        print(f"Board solvable: {is_solvable}")

        return is_solvable

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
            (-1, 0),   # hoch
            (1, 0),   # runter
            (0, -1),   # links
            (0, 1)    # rechts
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
        """Vergleiche das aktuelle Gameboard mit einem anderen."""
        return self.gameBoard == otherGameBoard

    def printGameBoard(self):
        """Print the current state of the gameboard in a readable format."""
        for row in self.gameBoard:
            print(row)

    def getCost(self):
        """Berechne die Gesamtkosten des aktuellen Zustands.
        Hier wird die Manhattan-Distanz verwendet.
        """
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


"""    def getMisplacedTilesCost(self):
        Calculate the cost based on the number of misplaced tiles.
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.gameBoard[i][j] != 0 and self.gameBoard[i][j] != Puzzle.goalState[i][j]:
                    cost += 1
        return cost

    def getManhattanCost(self):
        Calculate the cost based on the Manhattan distance.
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
        return cost"""