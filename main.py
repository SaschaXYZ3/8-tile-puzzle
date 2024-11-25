from puzzle import puzzle


def main():
    attempts = 0  # Counter for the number of boards generated

    while attempts < 1000:  # Keep generating game boards
        attempts += 1  # Increment attempt count
        myPuzzle = puzzle()  # Generate a new puzzle

        # Check if the board is solvable
        if not myPuzzle.is_solvable():
            # If the board is not solvable, print the details and break
            print("\nThis game board is NOT solvable!")
            myPuzzle.printGameBoard()
            print(f"\nNumber of game boards generated: {attempts}")
            return
    # If no unsolvable board is found after 1000 attempts
    print("\nAfter 1000 attempts, no unsolvable game board was generated.")

if __name__ == "__main__":
    main()
