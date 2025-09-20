# Unidriected Tree
# Unidriected Tree
un_tree = {
        'A': ['B', 'E'],
        'B': ['C', 'D', 'A'],
        'C': ['F', 'B'],
        'D': ['B'],
        'E': ['A'],
        'F': ['C']
    }




from collections import deque

def bidirectional(tree, start, goal):
    # Check if start and goal are the same
    if start == goal:
        return None, None

    # Lists to track visited nodes from start and goal
    start_visited = [start]
    goal_visited = [goal]

    # Queues to explore nodes from start and goal
    start_queue = deque([start])
    goal_queue = deque([goal])

    # Continue until queues are empty
    while start_queue and goal_queue:
        # Explore from start
        current_start = start_queue.popleft()
        for neighbor in tree[current_start]:
            if neighbor not in start_visited:
                start_visited.append(neighbor)
                start_queue.append(neighbor)

        # Explore from goal
        current_goal = goal_queue.popleft()
        for neighbor in tree[current_goal]:
            if neighbor not in goal_visited:
                goal_visited.append(neighbor)
                goal_queue.append(neighbor)

        # Check if paths meet
        if current_start in goal_visited or current_goal in start_visited:
            return start_visited, goal_visited

    return start_visited, goal_visited

# Example usage (assuming un_tree is defined)
print(bidirectional(un_tree, 'A', 'F'))