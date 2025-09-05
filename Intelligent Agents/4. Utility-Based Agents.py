# Initial state
state = {
    'A': 'dirty',
    'B': 'dirty',
    'current_room': 'A',
    'energy_used': 0,
    'cleanliness_score': 0
}

# Utility function: higher score is better
def utility(state):
    return state['cleanliness_score'] - state['energy_used']

# Simulate action on a copy of state
def simulate(state, action):
    new_state = state.copy()
    
    room = new_state['current_room']
    
    if action == 'suck' and new_state[room] == 'dirty':
        new_state[room] = 'clean'
        new_state['cleanliness_score'] += 10  # reward for cleaning
        new_state['energy_used'] += 1
    elif action == 'move':
        new_state['current_room'] = 'B' if room == 'A' else 'A'
        new_state['energy_used'] += 1  # moving costs energy
    
    return new_state

# Utility-based agent: chooses action with max utility
def utility_based_agent(state):
    possible_actions = ['suck', 'move']
    best_action = max(possible_actions, key=lambda a: utility(simulate(state, a)))
    return best_action

# Simulation loop
for _ in range(5):
    action = utility_based_agent(state)
    print(f"Action: {action}, State: {state}")
    
    # Apply the chosen action
    state = simulate(state, action)
    
    # Stop if all rooms are clean
    if state['A'] == 'clean' and state['B'] == 'clean':
        print("All rooms clean. Stopping.")
        break
