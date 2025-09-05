def simple_reflex_agent(percept):
    if percept == 'dirty':
        return 'suck'
    else:
        return 'move'




print(simple_reflex_agent('dirty'))