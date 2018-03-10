'''
Created on 1 Mar 2018

@author: Eimg
'''
import cmd
import math

class LEDTester(object):
    '''
    classdocs
    '''

    def __init__(self, N):
        '''
        Constructor
        '''
        self.lights = [[False]*N for i in range(N)]
        
    def size(self):
        count = 0
        for i in range(0, len(self.lights)):
            for val in self.lights[i]:
                count += 1
        return count
        
    def apply(self, instructions):
        cmd = instructions[0]
        if cmd == 'turn':
            cmd = instructions[1]
            start = instructions[2]
            end = instructions[4]
        elif cmd == 'switch':
            start = instructions[1]
            end = instructions[3]
            
        x = start.split(',')
        y = end.split(',')
        x1, y1, x2, y2 = self.assign_xy_values(x,y)
        
        if cmd == 'on':
            self.turnOn(self.size(), x1, y1, x2, y2)
        elif cmd == 'off':
            self.turnOff(self.size(), x1, y1, x2, y2)
        elif cmd =='switch':
            self.switch(self.size(), x1, y1, x2, y2)
        else:
            print('Command not recognised')
            
    def assign_xy_values(self, x, y):

        size = math.sqrt(self.size())
        if x[0] >= 0 and x[0] <= size:
            a= x[0]
        elif x[0] < 0:
            a = 0 
        elif x[0] > size:
            a = size
            
        if x[1] >= 0 and x[1] <= size:
            b =x[1]
        elif x[1] < 0:
            b = 0 
        elif x[1] > size:
            b = size
            
        if y[0] >= 0 and y[0] <= size:
            c =y[0]
        elif y[0] < 0:
            c = 0 
        elif y[0] > size:
            c = size
            
        if y[1] >= 0 and y[1] <= size:
            d =y[1]
        elif y[1] < 0:
            d = 0 
        elif y[1] > size:
            d = size
            
        return a, b, c, d   
       
    def count(self):
        count = 0
        for i in range(0, len(self.lights)):
            for j in range (0,len(self.lights[i])):
                if self.lights[i][j] == True:
                    print('Found light on')
                    count += 1
        return count
    
    def turnOn(self, N, x1, y1, x2, y2):
        for i in range (int(x1), int(x2)+1):
                for j in range(int(y1), int(y2)+1):
                    self.lights[i][j] = True
        print('Lights between (',x1,',',y1,') and (',x2,',',y2,') turned on')
                
    def turnOff(self, N, x1, y1, x2, y2):
        for i in range (int(x1), int(x2)+1):
                for j in range(int(y1), int(y2)+1):
                    self.lights[i][j] = False
        print('Lights between (',x1,',',y1,') and (',x2,',',y2,') turned off')
        
    def switch(self, N, x1, y1, x2, y2):
        for i in range (int(x1), int(x2)+1):
                for j in range(int(y1), int(y2)+1):
                    if self.lights[i][j] == False:
                        self.lights[i][j] = True
                    elif self.lights[i][j] == True:
                        self.lights[i][j] = False
        print('Lights between (',x1,',',y1,') and (',x2,',',y2,') toggled')