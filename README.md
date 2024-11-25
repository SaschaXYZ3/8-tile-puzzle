# 8-tile-puzzle

# Schlachtplan

1. Random Zahlen dürfen nur 1 mal vorkommen und befüllen ein 3x3 array
2. Was ist das ziel ? wo soll die 0 am Schluss stehen
3. check ob diese random zahlen überhaupt lösbar sind?
	1. inversions
4. manhattan und hamming distance als A* Algorithmus heuristisch
	1. successors also eine liste wieviele hops es gibt und was am wenigsten hops braucht ganz oben
	2. costs mit manhattan oder hamming
	3. successors in eine queue mit heapq
	4. queue abfragen 
	5. pfad abfragen
	6. umsetzen
5. Statistik wieviele nodes notwendig waren, wie die laufzeit ist usw
6. user interface (command line zb)

Anwendung von Mathe
KPIs ausgeben in der Console