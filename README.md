# 8-Tile Puzzle

## Schlachtplan

- [x] **1. Random Zahlen dürfen nur 1 mal vorkommen und befüllen ein 3x3 Array.**
- [x] **2. Was ist das Ziel? Wo soll die 0 am Schluss stehen?**
        0 soll links oben stehen
- [x] **3. Check, ob diese Random-Zahlen überhaupt lösbar sind:**
  - [x] Berechnung der Inversions.
- [x] **4. Manhattan- und Hamming-Distanz als Heuristik für den A*-Algorithmus:**
  - [x] Generieren von Successors (Liste mit allen möglichen Moves).
  - [x] Kostenberechnung mit Manhattan- oder Hamming-Distanz.
  - [x] Hinzufügen der Successors in eine Queue mit `heapq`.
  - [x] Abfragen der Queue.
  - [x] Pfadberechnung (optimaler Pfad finden).
  - [x] Umsetzen des Pfades auf das Spielfeld.
- [x] **5. Statistik:** Wie viele Nodes wurden benötigt, wie ist die Laufzeit etc.?
- [x] **6. User Interface (z. B. Command Line):**

---


## Overview
This project implements a solution to the 8-tile puzzle problem using the A* search algorithm. The implementation includes two heuristic functions (Hamming and Manhattan distances) to evaluate the puzzle's state during the search. The code is modular, allowing for comparisons of different heuristics and extensibility for future enhancements.

---

## File Descriptions

### `main.py`
- **Purpose**: Entry point of the program.
- **Key Functions**:
  - Initializes the puzzle and displays its current state.
  - Solves the puzzle using the A* algorithm.
  - Allows the user to compare the performance of Manhattan and Hamming heuristics.
- **How to Run**: Execute this file to start the program. It interacts with the user via command-line input.

### `Puzzle.py`
- **Purpose**: Defines the `Puzzle` class for managing the puzzle game board.
- **Key Features**:
  - Generate solvable puzzles.
  - Compute valid moves for the blank tile.
  - Check if the current state matches the goal state.
  - Utility methods like copying the board and calculating Manhattan distance.

### `AStarQueue.py`
- **Purpose**: Implements the A* search algorithm for solving the puzzle.
- **Key Features**:
  - Manages open and closed nodes.
  - Calculates costs based on the chosen heuristic.
  - Traces and prints the solution path.

### `Nodes.py`
- **Purpose**: Defines the `Nodes` class, representing each node in the search tree.
- **Key Features**:
  - Stores the current board state, parent node, and heuristic costs (`gCost`, `hCost`, and `fCost`).
  - Includes methods for managing child nodes.

### `Heuristic.py`
- **Purpose**: Implements heuristic functions for evaluating puzzle states.
- **Key Heuristics**:
  - **Hamming Distance**: Counts the number of misplaced tiles.
  - **Manhattan Distance**: Calculates the sum of distances of tiles from their target positions.

### `utils.py`
- **Purpose**: Contains utility functions for displaying the board and solving puzzles.
- **Key Features**:
  - `display_board`: Displays the puzzle state in a readable format.
  - `solve_puzzle`: Solves the puzzle using a given heuristic.

### `benchmark.py`
- **Purpose**: Contains functionality to compare the performance of heuristics.
- **Key Features**:
  - Runs the A* algorithm multiple times on randomly generated puzzles.
  - Calculates and displays average time and expanded nodes for each heuristic.

### `testcases.py`
- **Purpose**: Provides predefined test cases for validating the solver.
- **Key Features**:
  - Contains edge cases, solvable puzzles, and unsolvable puzzles for testing.

---

## Design Decisions

### 1. **Modular Code Structure**
The project is structured modularly to ensure reusability and readability. Each major functionality is implemented in a separate file:
- **`Puzzle.py`**: Contains the logic for representing and manipulating the game board.
- **`AStarQueue.py`**: Implements the A* search algorithm.
- **`Heuristic.py`**: Implements the heuristic functions (Manhattan and Hamming).
- **`utils.py`**: Contains utility functions such as board display and solving the puzzle.
- **`benchmark.py`**: Facilitates performance comparisons of the heuristics.
- **`testcases.py`**: Includes test cases to verify the functionality.

This structure simplifies future extensions and changes to the project.

---

### 2. **Admissible Heuristics**
To solve the 8-puzzle problem, two **admissible heuristics** were implemented:
- **Manhattan Distance**: Calculates the sum of the vertical and horizontal moves required to reach the goal state.
- **Hamming Distance**: Counts the number of tiles out of place compared to the goal state.

The modular design allows adding new heuristics with minimal changes to the existing codebase.

---

### 3. **A* Search Implementation**
The A* algorithm was chosen for its optimality and efficiency. The `AStarQueue` class implements:
- A priority queue using `heapq` to manage open nodes.
- Node tracking to avoid redundant state expansions.
- Efficient path tracing from the goal state back to the start.

The implementation ensures correctness while providing flexibility to adapt to other admissible heuristics.

---

### 4. **Random Solvable Puzzle Generation**
The `Puzzle` class ensures only solvable puzzles are generated using the inversion count method. This avoids wasting computational resources on unsolvable states. 

---

### 5. **Benchmarking and Comparison**
The `benchmark.py` module was created to compare the performance of different heuristics. Key metrics include:
- **Average runtime**: Measures the efficiency of each heuristic.
- **Nodes expanded**: Indicates the search space explored by each heuristic.

This approach provides a quantitative analysis to justify the choice of heuristics.

---

### 6. **Focus on Readability and Maintainability**
- Descriptive class and function names to improve code readability.
- Extensive comments and docstrings to explain the purpose of each module, function, and variable.
- Separation of concerns to avoid tightly coupled components, enabling easier debugging and testing.

---

### 7. **Unit Testing**
The `testcases.py` file contains unit tests to verify core functionalities like heuristic calculations, puzzle generation, and the A* algorithm. This ensures reliability and correctness across all components.

---

### 8. **Error Handling and Debugging**
- The `Puzzle` class logs details about the generated boards and their solvability.
- Debugging statements are included in critical sections, such as node expansion in `AStarQueue`, to trace the algorithm's behavior.

---

### 9. **Interactive User Experience**
The `main.py` provides:
- A clear display of the current puzzle.
- Options for solving the puzzle using a selected heuristic.
- The ability to compare heuristics interactively with user-defined trial counts.

This ensures a user-friendly interface for both demonstration and testing purposes.

---

### 10. **Efficiency Optimization**
The implementation minimizes redundant calculations:
- Node states are stored in a set to avoid duplicate expansions.
- Heuristic calculations are reused wherever possible.
- The A* algorithm terminates early when the goal state is found.

This design ensures an optimal balance between performance and readability.
---


## Class Descriptions

### `Puzzle`
- **Attributes**:
  - `goalState`: The goal configuration of the puzzle.
  - `gameBoard`: The current state of the puzzle board.
- **Methods**:
  - `createRandomGameBoard`: Generates a random solvable puzzle.
  - `isSolvable`: Checks if a puzzle configuration is solvable based on inversion count.
  - `isGoalReached`: Verifies if the current state matches the goal state.
  - `generatePossibleMoves`: Generates all possible moves for the blank tile.

### `AStarQueue`
- **Attributes**:
  - `puzzle`: The initial puzzle state.
  - `heuristicClass`: The heuristic function used to evaluate states.
  - `nodes`: A dictionary to store nodes by their IDs.
  - `openNodes`: Priority queue for open nodes.
- **Methods**:
  - `setFirstNode`: Initializes the first node in the search tree.
  - `findSolution`: Runs the A* algorithm to find a solution.
  - `expandNode`: Expands a node to generate its children.
  - `getPath`: Traces the path from a node to the root.

### `Nodes`
- **Attributes**:
  - `nodeId`: Unique identifier for the node.
  - `parent`: Parent node ID.
  - `puzzle`: Current puzzle state.
  - `gCost`, `hCost`, `cost`: Cost attributes for A*.
- **Methods**:
  - `addChild`: Links a child node to the parent.

### `Heuristic`
- **HammingDistance**:
  - Counts tiles that are not in their goal positions.
- **ManhattanDistance**:
  - Calculates the sum of distances of tiles from their goal positions.

---

## Theoretical Explanation of Heuristics

### **Hamming Distance**
- **Definition**: Counts the number of misplaced tiles (excluding the blank tile).
- **Purpose**: Provides a simplistic heuristic to estimate the number of moves required to solve the puzzle.
- **Formula**: 
  \[
  H = \sum_{i=1}^{n} \text{misplaced}(i)
  \]
  where `misplaced(i)` is 1 if tile \(i\) is not in its target position, otherwise 0.

### **Manhattan Distance**
- **Definition**: Calculates the total number of moves required for each tile to reach its goal position if it could move independently.
- **Purpose**: More precise than Hamming, considering the actual distances of tiles.
- **Formula**:
  \[
  M = \sum_{i=1}^{n} \left( |x_i - x_{\text{goal}}| + |y_i - y_{\text{goal}}| \right)
  \]
  where \((x_i, y_i)\) is the current position of tile \(i\), and \((x_{\text{goal}}, y_{\text{goal}})\) is its target position.

---

## Performance Analysis

### **Average and Mean Calculations**
- **Average Time**: Sum of all runtimes divided by the number of trials.
- **Mean Nodes Expanded**: Sum of expanded nodes across all trials divided by the number of trials.

### **Formula**:
- Average Time:
  \[
  \text{Avg Time} = \frac{\sum_{i=1}^n \text{Time}_i}{n}
  \]
- Average Nodes:
  \[
  \text{Avg Nodes} = \frac{\sum_{i=1}^n \text{Nodes}_i}{n}
  \]

---

## Class Diagram

```plaintext
@startuml
class Puzzle {
  - goalState: List[List[int]]
  - gameBoard: List[List[int]]
  + createRandomGameBoard()
  + isSolvable(gameBoard): bool
  + isGoalReached(): bool
  + generatePossibleMoves(): List[List[List[int]]]
  + printGameBoard(): void
}

class AStarQueue {
  - puzzle: Puzzle
  - heuristicClass: Heuristic
  - nodes: Dict[int, Nodes]
  - openNodes: List[Nodes]
  + setFirstNode(): void
  + findSolution(): void
  + expandNode(nodeId: int): void
  + getPath(nodeId: int): List[int]
}

class Nodes {
  - nodeId: int
  - parent: int
  - puzzle: Puzzle
  - gCost: int
  - hCost: int
  - cost: int
  + addChild(childId: int): void
}

class Heuristic {
  + calculate(gameBoard: List[List[int]]): int
}

class HammingDistance {
  + calculate(gameBoard: List[List[int]]): int
}

class ManhattanDistance {
  + calculate(gameBoard: List[List[int]]): int
}

Puzzle "1" --> "1" AStarQueue
AStarQueue "1" --> "*" Nodes
AStarQueue "1" --> "1" Heuristic
Heuristic <|-- HammingDistance
Heuristic <|-- ManhattanDistance
@enduml
```
___

# Theoretical Explanation of 8-Puzzle Solvability



## 1. What Is an Inversion?

- An **inversion** occurs when a pair of tiles \((i, j)\) exists such that:
  - \(i > j\), but \(i\) appears **before** \(j\) in the flattened list of the puzzle.
  - The blank tile (0) is ignored when counting inversions.

### Example:
Flattened board: `[1, 8, 2, 0, 4, 5, 3, 7, 6]`

- Ignoring the blank tile, the list is: `[1, 8, 2, 4, 5, 3, 7, 6]`.
- Count inversions:
  - \(8 > 2\): 1 inversion.
  - \(8 > 4\): 1 inversion.
  - \(8 > 5\): 1 inversion.
  - \(8 > 3\): 1 inversion.
  - \(8 > 7\): 1 inversion.
  - \(8 > 6\): 1 inversion.
  - \(5 > 3\): 1 inversion.
  - \(7 > 6\): 1 inversion.
- Total inversions: \(10\).

---

