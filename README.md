# 8-Tile Puzzle

## Schlachtplan

- [x] **1. Random Zahlen dürfen nur 1 mal vorkommen und befüllen ein 3x3 Array.**
- [ ] **2. Was ist das Ziel? Wo soll die 0 am Schluss stehen?**
- [ ] **3. Check, ob diese Random-Zahlen überhaupt lösbar sind:**
  - [ ] Berechnung der Inversions.
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
