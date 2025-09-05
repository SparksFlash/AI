# Goal-based agent example with 2 rooms: A and B
goal = 'clean_all_rooms'

# State keeps track of room status
state = {'A': 'dirty', 'B': 'dirty', 'current_room': 'A'}

def goal_based_agent(state):
    room = state['current_room']
    
    # If current room is dirty, clean it
    if state[room] == 'dirty':
        state[room] = 'clean'
        return 'suck'
    
    # If goal is achieved, stop
    if all(status == 'clean' for r, status in state.items() if r != 'current_room'):
        return 'stop'
    
    # Move to next room if current is clean
    next_room = 'B' if room == 'A' else 'A'
    state['current_room'] = next_room
    return f'move_to_{next_room}'

# Simulation loop
for _ in range(5):
    action = goal_based_agent(state)
    print(f"Action: {action}, State: {state}")
