from heapq import heappop, heappush

def a_star(start, goal):
    open_list = []
    heappush(open_list, (0, start, [start]))
    visited = set()
    while open_list:
        cost, node, path = heappop(open_list)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, step_cost in get_neighbors(node):
                new_cost = cost + step_cost + heuristic(neighbor, goal)
                heappush(open_list, (new_cost, neighbor, path + [neighbor]))

def heuristic(node, goal):
    return abs(goal - node)  # Example heuristic

def get_neighbors(node):
    return [(node - 1, 1), (node + 1, 1)]  # Dummy neighbors
