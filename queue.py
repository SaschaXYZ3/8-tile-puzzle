import heapq
import time
import sys
from puzzle import Puzzle

# A* Algorithm number of nodes expanded
def a_star(puzzle, heuristic):
    start_time = time.time()   # start timer
    open_list = []            # Priority Queue for the minimum f(n)-value
    closed_list = set()       # for expanded nodes
    heapq.heappush(open_list, (0, puzzle.gameBoard, 0))   # f_cost, board, g_cost
    nodes_expanded = 0        # count for expanded nodes

    while open_list:    # take the node with the minimum f_cost
        f_cost, current_board, g_cost = heapq.heappop(open_list)
        current_puzzle = Puzzle(current_board)

        #print(f"Open list memory: {open_list_memory} bytes")
        #print(f"Closed list memory: {closed_list_memory} bytes")

        if current_puzzle.isGoalReached(): # check if goal is reached
            end_time = time.time()  # end timer
            runtime = end_time -start_time # calculate runtime
            # calculate storage of both lists
            open_list_memory = sum(sys.getsizeof(item) for item in open_list)
            closed_list_memory = sum(sys.getsizeof(item) for item in closed_list)
            memory_usage = open_list_memory + closed_list_memory
            return {
                "path_cost": g_cost,
                "nodes_expanded": nodes_expanded,
                "solution": current_board,
                 "runtime": runtime,
                "memory_usage": memory_usage / (1024 ** 2),  # memory in MB
            }
         # add actuall state to closed_list
        closed_list.add(tuple(map(tuple,current_board)))

        # generate neighbors and check
        for neighbor in current_puzzle.generatePossibleMoves():
            neighbor_tuple = tuple(map(tuple,neighbor))
            if neighbor_tuple in closed_list:
                continue    # continue already achieved states

            # calculate g,h and f for neighbor
            g_neighbor = g_cost + 1         # every movement costs 1
            h_neighbor = heuristic(Puzzle(neighbor))
            f_neighbor = g_neighbor + h_neighbor

            # put neighbours into the open_list
            heapq.heappush(open_list, (f_neighbor, neighbor, g_neighbor))
            nodes_expanded += 1