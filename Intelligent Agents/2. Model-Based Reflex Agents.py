state = {'room_dirty': True}

def model_based_agent(percept):
    state['room_dirty'] = percept == 'dirty'
    if state['room_dirty']:
        return 'suck'
    else:
        return 'move'


print(model_based_agent('clean'))