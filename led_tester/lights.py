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
        if instructions == None:
            return
        instructions = [s.strip() for s in instructions]
        cmd = instructions[0]
        if cmd == 'turn':
            cmd = instructions[1]
            start = instructions[2]
            end = instructions[4]
        elif cmd == 'switch':
            start = instructions[1]
            end = instructions[3]
        else:
            print('Command not recognised')
            return
        
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
        x1 = int(x[0])
        x2 = int(y[0])
        y1 = int(x[1])
        y2 = int(y[1])
        size = int(math.sqrt(self.size()))
        if x1 >= 0 and x1 <= size:
            a = x[0]
        elif x1 < 0:
            a = str(0)
        elif x1 > size:
            a = str(size-1)
            
        if y1 >= 0 and y1 <= size:
            b =x[1]
        elif y1 < 0:
            b = str(0)
        elif y1 > size:
            b = str(size-1)
            
        if x2 >= 0 and x2 <= size:
            c =y[0]
        elif x2 < 0:
            c = str(0) 
        elif x2 > size:
            c = str(size-1)
            
        if y2 >= 0 and y2 <= size:
            d =y[1]
        elif y2 < 0:
            d = str(0)
        elif y2 > size:
            d = str(size-1)
            
        return a, b, c, d   
       
    def count(self):
        count = 0
        for i in range(0, len(self.lights)):
            for j in range (0,len(self.lights[i])):
                if self.lights[i][j] == True:
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