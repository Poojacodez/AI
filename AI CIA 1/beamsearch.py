def beam_search(start, goal, beam_width):
    open_list = [(start, [start])]  # nodes and their paths
    while open_list:
        open_list = sorted(open_list, key=lambda x: heuristic(x[0], goal))[:beam_width]
        for node, path in open_list:
            if node == goal:
                return path
            for neighbor in get_neighbors(node):
                open_list.append((neighbor, path + [neighbor]))
    return None

def heuristic(node, goal):
    return abs(goal - node)  # Example heuristic

def get_neighbors(node):
    return [node - 1, node + 1]  # Dummy neighbors
