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
   - **`getManhattanCost`**: Berechnet die Summe der Manhattan-Distanzen aller Kacheln von ihren Zielpositionen.

8. **Spielfeldoperationen**
   - **`copyGameBoard`**: Erstellt eine Kopie des aktuellen Spielfelds.
   - **`getEmptyPosition`**: Findet die Position des leeren Felds (0).
   - **`generatePossibleMoves`**: Generiert alle möglichen Spielfeldkonfigurationen, die durch Verschieben des leeren Felds entstehen können.
