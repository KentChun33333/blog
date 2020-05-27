# -*- coding: utf-8 -*-

"""
Policy : P
Value : V(s)
"""

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
    WIDTH=1200
    HEIGHT = 800
# get monitor resolution 


# Set Pixel Unit 
UNIT = int(0.1 * min(WIDTH, HEIGHT))

class GridWord(tk.Tk):
    def __init__(self, 
                 width, 
                 height,
                 # list of turple
                 trapped_position=[(2,2),(4,3),(2,4)],
                 end_position = (3,4), 
                 fruit_position = [(4,2),], 
                 is_many_terminal = True):
        # =============================================
        global UNIT 
        super(GridWord, self).__init__()
        self.size = (width, height)
        self.S = np.zeros((width, height))

        self.action_space = (0, 1 , 2, 3)
        self.position = [1,1]
        self.ratio = 0
        self.pre_position = []
        self.fruit_position = fruit_position
        self.trapped_position = trapped_position
        x, y = end_position 
        if x>width or y > height:
            self.end_position = (width, height)
        else:
            self.end_position = end_position
        self.nS = len(self.S.flatten())
        self.nA = len(self.action_space)

        # visualization 
        self._vis() 
        self.logger = DebugLog('test')
        self.episode = 0
        self.sussess = 0
        # many ternimal 
        assert type(is_many_terminal) == bool
        self.many_ternimal = is_many_terminal 

      
    def step(self, action):
        state = self.position
        action = float(action)
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
        self.squeez_state_nor()

        done = self.is_terminated()
        reward = self.give_reward()
        # return list instead of tuple for conculation 
        return np.array([self.nor_position]),reward, done, {}

    def reset(self):
        self.position = [1,1]
        # init observation or state
        # return array type for count 
        # get new nor_position as observation
        self.squeez_state_nor()
        return np.array([self.nor_position])
    
    def give_reward(self):
        # =================================================
        # keep reward always positive is to encourage 
        # to keep working 
        # ------ :: or :: ------
        # keep reward always negativ is to encourage
        # finding the terminal ASAP
        # =================================================
        temp = -0.01
        if tuple(self.position) == self.end_position:
            temp += 1.
            self.sussess+=1.
            ratio = round(self.sussess / (self.episode+ 1e-5),5)
            # 
            self.logger.warn('Reach Goal at EP:{}'
                ' WinRate : {}'.format(self.episode, ratio))
        elif self.is_out == True :
            temp -= .35
        elif tuple(self.position) in self.fruit_position:
            temp += .8
        # [Note]
        # Regulation Penalizes the behavior of force and back 
        # this is the case if you give a small positive reward to encourage keep moving
        # [Note]
        # if pre_position == position : it means you are not allowed to move that way
        if self.pre_position == self.position or self.position == self.pre_pre_position:
            # 
            temp -= .5
        # ==================================================
        # [Note]
        # Use the float type
        return temp

    def is_terminated(self):
        if tuple(self.position) == self.end_position or self.is_out()==True:
            self.episode +=1
            return True
        return False

    def is_out(self):
        if tuple(self.position) in self.trapped_position:
            return self.many_ternimal 

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

        # place fruit 
        for i in self.fruit_position:
            x1,y1,x2,y2 = self.get_corrdinate(i)
            self.canvas.create_oval(x1,y1,x2,y2,fill='blue')
        
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

    def squeez_state_nor(self):
        """
        return np.ravel_multi_index(self.position, self.size)
        which np.ravel is equal to tf.squeez ( for flatten)
        [usage]
        run before any return self.postion 
        """
        x,y = self.position
        self.nor_position = np.ravel_multi_index((max(0,x-1),max(0,y-1)), self.size)
        
        
if __name__=='__main__':
    ENV = GridWord(6,6)
    ENV.step(1)
    print (ENV.position)
    ENV.step(1)
    print (ENV.position)      
    

    