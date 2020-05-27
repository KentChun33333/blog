'''
Author : Kent Chiu 
Environment as the Problems
'''

class Agent(object):
    def __init__():
        pass

    @property
    def action():
        pass

    @property
    def observatons():
        pass

    @property
    def objective():
        pass

class Environment(object):
    def __init__():
        pass

    def construct():
        pass

    def reset():
        '''
        Epsode Reset 
        '''
        pass

    def rules():
        pass

class MAZE(Environment):
    def __init__(self, length, actionSet):
        # Multi-inherit
        super(Environment, self).__init__()
        self.actionSet = {'UP':1, 'RT':2, 'DW':3,'LF':4}

    def step(self, action):
        assert action in self.actionSet
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

    def construct():

    def _put_stone():x
        pass

    def _put_holes():
        pass

    def _put_fruit():
        pass

    def _put_




