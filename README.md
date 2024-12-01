# 8-Tile Puzzle

## Schlachtplan

- [x] **1. Random Zahlen dürfen nur 1 mal vorkommen und befüllen ein 3x3 Array.**
- [x] **2. Was ist das Ziel? Wo soll die 0 am Schluss stehen?**
        0 soll links oben stehen
- [x] **3. Check, ob diese Random-Zahlen überhaupt lösbar sind:**
  - [x] Berechnung der Inversions.
- [ ] **4. Manhattan- und Hamming-Distanz als Heuristik für den A*-Algorithmus:**
  - [ ] Generieren von Successors (Liste mit allen möglichen Moves).
  - [ ] Kostenberechnung mit Manhattan- oder Hamming-Distanz.
  - [ ] Hinzufügen der Successors in eine Queue mit `heapq`.
  - [ ] Abfragen der Queue.
  - [ ] Pfadberechnung (optimaler Pfad finden).
  - [ ] Umsetzen des Pfades auf das Spielfeld.
- [ ] **5. Statistik:** Wie viele Nodes wurden benötigt, wie ist die Laufzeit etc.?
- [ ] **6. User Interface (z. B. Command Line):**

---

## Anwendung von Mathe
KPIs in der Konsole ausgeben.


### Klasse Puzzle.py

1. **Zielzustand (`goalState`)**
   - Definiert die Zielkonfiguration des Spielfelds:
     ```
     [[0, 1, 2],
      [3, 4, 5],
      [6, 7, 8]]
     ```
   - Das leere Feld (0) befindet sich oben links.

2. **Initialisierung (`__init__`)**
   - Erstellt ein Puzzle-Objekt mit einem vorgegebenen oder zufällig generierten Spielfeld.
   - Wenn kein Spielfeld angegeben wird, wird ein zufälliges, lösbares Spielfeld erzeugt.

3. **Zufällige Spielfeldgenerierung (`createRandomGameBoard`)**
   - Generiert eine zufällige und lösbare Konfiguration des Spielfelds.
   - Nutzt die `isSolvable`-Methode, um sicherzustellen, dass das Spielfeld lösbar ist.

4. **Spielfeldanzeige (`printGameBoard`)**
   - Gibt das aktuelle Spielfeld in lesbarer Form auf der Konsole aus.

5. **Lösbarkeit prüfen (`isSolvable`)**
   - Überprüft, ob die aktuelle Spielfeldkonfiguration lösbar ist, basierend auf der Anzahl von Inversionen.

6. **Zielzustand prüfen (`isGoalReached`)**
   - Vergleicht das aktuelle Spielfeld mit dem Zielzustand und gibt zurück, ob dieser erreicht wurde.

7. **Kostenberechnung**
   - **`getMisplacedTilesCost`**: Zählt die falsch platzierten Kacheln im Vergleich zum Zielzustand.
   - **`getCost`**: Berechnet die Summe der Manhattan-Distanzen aller Kacheln von ihren Zielpositionen.

8. **Spielfeldoperationen**
   - **`copyGameBoard`**: Erstellt eine Kopie des aktuellen Spielfelds.
   - **`getEmptyPosition`**: Findet die Position des leeren Felds (0).
   - **`generatePossibleMoves`**: Generiert alle möglichen Spielfeldkonfigurationen, die durch Verschieben des leeren Felds entstehen können.



**A_star-Algorithmus Implementierung:**
--> Prioritätswarteschlange wird verwendet, um effizient den besten Knoten zu finden
f(n) = g(n) + h(n)
g(n): Kosten des Pfades vom Startknoten n (Anzahl der Movements)
h(n): Heuristik (Schätzung der verbleibenden Kosten zum Ziel)

___

# Theoretical Explanation of 8-Puzzle Solvability

## 1. Key Solvability Rule

For a **3x3 grid** (8-puzzle), a puzzle is **solvable** if:

1. The **number of inversions** is even **and** the **blank tile is on an odd row (from the bottom, 1-indexed)**.
2. The **number of inversions** is odd **and** the **blank tile is on an even row (from the bottom, 1-indexed)**.

This rule ensures the puzzle can be solved by swapping tiles while maintaining the necessary parity constraints.

---

## 2. What Is an Inversion?

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

## 3. Why Does the Blank Tile's Position Matter?

The **blank tile's position** affects solvability due to the way tiles are shifted during the solving process:

- The blank tile acts as a "helper" to facilitate tile swaps.
- Its row position determines whether the puzzle's inversion parity aligns with a valid solution.

### Parity Impact:
1. **Odd Row (from bottom)**:
   - Does not alter inversion parity.
2. **Even Row (from bottom)**:
   - Alters inversion parity.

This additional constraint is unique to **odd-sized grids** like 3x3 puzzles.

---

## 4. Why Not Just Inversion Count?

For **even-sized grids** (e.g., 4x4 puzzles):
- The inversion count alone determines solvability, as the grid size allows for unrestricted parity adjustments.

For **odd-sized grids** (e.g., 3x3 puzzles):
- The blank tile's position becomes a necessary factor because the grid's size limits the freedom of tile movement, enforcing stricter parity constraints.

---

## 5. Solvability Rule Summary

### A puzzle is solvable if:
- The **number of inversions** is **even**, and the blank tile is on an **odd row (from the bottom)**.
- The **number of inversions** is **odd**, and the blank tile is on an **even row (from the bottom)**.

### A puzzle is unsolvable if:
- The **number of inversions** is **even**, and the blank tile is on an **even row (from the bottom)**.
- The **number of inversions** is **odd**, and the blank tile is on an **odd row (from the bottom)**.

---

## 6. Examples of Solvability

### Example 1: Solvable
- Flattened board: `[1, 8, 2, 0, 4, 5, 3, 7, 6]`
- Inversions: \(10\) (Even)
- Blank row (from bottom): \(2\) (Odd)
- **Result**: Solvable.

### Example 2: Unsolvable
- Flattened board: `[1, 8, 2, 4, 0, 5, 3, 7, 6]`
- Inversions: \(11\) (Odd)
- Blank row (from bottom): \(1\) (Odd)
- **Result**: Unsolvable.

---

## 7. Testing the Rule in Code

### Implementation in Python

```python
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

    # Solvability check
    is_even_inversions = inversions % 2 == 0
    is_odd_row = blank_row_from_bottom % 2 == 1
    is_solvable = (is_even_inversions and is_odd_row) or (not is_even_inversions and not is_odd_row)

    return is_solvable