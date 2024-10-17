def oracle_search(start, goal):
    path = []
    while start != goal:
        next_node = oracle_step(start, goal)
        path.append(next_node)
        start = next_node
    return path

def oracle_step(current, goal):
    return current + 1