# Kent Chiu

import numpy as np
import os
from common_log import DebugLog

try:
    import tkinter as tk
except :
    import Tkinter as tk

if os.name =='nt':
    from win32api import GetSystemMetrics
    WIDTH = GetSystemMetrics(0)
    HEIGHT = GetSystemMetrics(1)
else:
    WIDTH = 1000
    HEIGHT = 750
# Global Variables
# Set Pixel Unit
UNIT = int(0.05 * min(WIDTH, HEIGHT))

class GridWord(tk.Tk):
    '''description :
    this is a 2D GridWord as an ENV for Reinforcement Learning
    '''
    def __init__(self,
        width, height,
        trapped_position=[(2,2),(4,3),(2,4)],
        end_position = (3,4),
        fruit_position = ()):
        '''
        '''

        global UNIT
        super(GridWord, self).__init__()
        self.size = (width, height)
        self.S = np.zeros((width, height))

        # Not really :: if we use Policy Gradient
        #     Action_space better -1 ~ 1 or 0 ~ 1
        # Since we could use max(index of probability-distribution)
        # ==============================================================
        self.action_space = (0, 1 , 2, 3)
        self.position = [1,1]
        self.pre_position = []
        self.pre_pre_position = []
        self.ratio = 0

        # ==============================================================
        # [Note:1]
        # ==============================================================
        # Aware of using list is with dimension expension risk
        # Better to use tuple in this case
        # Also aware of using tuple is not assignable
        # ==============================================================
        # [Note:2]
        # ==============================================================
        # To use Policy Gradient :: Might be aware of we could take any
        # action at the first step to make sure the smoothness of the
        # learning process, otherwise it would stop immediately
        # ==============================================================

        self.trapped_position = trapped_position
        x, y = end_position
        if x>width or y > height:
            self.end_position = (width, height)
        else:
            self.end_position = end_position
        self.nS = len(self.S.flatten())
        self.observation_space = self.S
        self.nA = len(self.action_space)

        # visualization
        self._vis()
        self.logger = DebugLog('test')
        self.episode = 0
        self.sussess = 0


    def step(self, action):
        state = self.position
        # if out of boundery, we could just not move our current states
        # due to a forbidden action,
        # :: or ::
        # we could go move-and-done but which is not a good way
        # because it would cause a block-effect on edge-position
        if action == self.action_space[0] :
            if state[1]>0:
                state[1]-=1
        elif action == self.action_space[1] :
            if state[0]<self.size[0]:
                state[0]+=1
        elif action == self.action_space[2] :
            if state[1]<self.size[1] :
                state[1]+=1
        elif action == self.action_space[3] :
            if state[0] > 0:
                state[0]-=1
        # update the position to the next_state
        self.pre_position = self.position
        self.pre_pre_position = self.pre_position
        self.position = state
        self.state_normalize()

        done = self.is_terminated()
        reward = self.give_reward()
        # return list instead of tuple for conculation
        return np.array(self.nor_position),reward, done, {}

    def reset(self):
        '''description:
        init observation/state and return array type for count.
        '''
        self.position = [1,1]

        # get new nor_position as observation
        self.state_normalize()
        return np.array(self.nor_position)

    def is_terminated(self):
        tmp = tuple(self.position)
        if tmp == self.end_position or tmp in self.trapped_position:
            self.episode +=1
            return True
        return False

    def give_reward(self):

        # =================================================
        # keep reward always positive is to encourage
        # to keep working
        # ------ :: or :: ------
        # keep reward always negativ is to encourage
        # finding the terminal ASAP
        # =================================================
        temp = -0.0000001
        if tuple(self.position) == self.end_position:
            temp += 1.
            self.sussess+=1.
            self.ratio = round(self.sussess / (self.episode+ 1e-5),5)
            # ===========================================================
            # [Note]
            # ===========================================================
            # if there are fails terminated position
            # it is worth to evaluate the ratio of good/winning rate
            # which representing how frequent we end at good terminals
            # ===========================================================
            self.logger.warn('Reach Goal at EP:{}'
                ' WinRate : {}'.format(self.episode, self.ratio))
        # [Note]
        # Regulation Penalizes the behavior of force and back
        # this is the case if you give a small positive reward to encourage keep moving
        # [Note]
        # if pre_position == position : it means you are not allowed to move that way
        if self.pre_position == self.position or self.position == self.pre_pre_position:
            #
            temp -= .5
        if self.position in self.trapped_position:
            temp -=.8
        # ==================================================
        # [Note]
        # Use the float type
        return temp

    def is_out(self):
        if tuple(self.position) in self.trapped_position:
            return False
        x, y = self.position
        if x > self.size[0] or y > self.size[1] or x < 0 or y <0 :
            return False
        # not sure about this
        return False

    def _vis(self):
        # call with instance
        # draw background
        MAZE_W, MAZE_H = self.size
        self.canvas = tk.Canvas(self, bg='white',height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)
        # create grids
        for c in range(0, self.size[0] * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, self.size[1] * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # place hole
        for j in self.trapped_position:
            x1,y1,x2,y2 = self.get_corrdinate(j)
            self.canvas.create_rectangle(x1,y1,x2,y2,fill='black')

        # place goal
        x1,y1,x2,y2 = self.get_corrdinate(self.end_position)
        self.canvas.create_oval(x1,y1,x2,y2,fill='yellow')

        # place current position
        x1, y1, x2, y2 = self.get_corrdinate(self.position)
        self.position_vis = self.canvas.create_oval(x1,y1,x2,y2,fill='red')
        self.canvas.pack()
        # visualize it
        # this is forever but would cause a pause problem
        # self.mainloop()
        # =============================================
        # this is update which is associated with step
        self.update()

    def render(self):
        # call after each action or step
        self.canvas.delete(self.position_vis)
        x1, y1, x2, y2 = self.get_corrdinate(self.position)
        self.position_vis = self.canvas.create_oval(x1,y1,x2,y2,fill='red')
        self.canvas.pack()
        self.update()

    def get_corrdinate(self, position):
        x2,y2 = position
        x2 *= UNIT
        y2 *= UNIT
        x1, y1 = x2-UNIT, y2-UNIT
        return x1,y1,x2,y2

    def state_normalize(self):
        # run before any return self.postion
        # =====================================================================
        # [Note]
        # =====================================================================
        # it is always better to do reasonable normalization before any ops,
        # like the core concept of Batch Normalization, it is better to have a
        #
        x,y = self.position
        self.nor_position = [float(x/self.size[0]), float(y/self.size[1])]

if __name__=='__main__':
    ENV = GridWord(6,6)
    ENV.step(1)
    print (ENV.position)
    ENV.step(1)
    print (ENV.position)


####################################################################
# turn 2-dim state to 1 dim by
# new_state = np.ravel_multi_index(tuple(new_position), self.shape)
