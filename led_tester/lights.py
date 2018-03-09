'''
Created on 1 Mar 2018

@author: Eimg
'''
import cmd

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
        x1, x2, y1, y2 = x[0], y[0], x[1], y[1]
        
        if cmd == 'on':
            self.turnOn(self.size(), x1, y1, x2, y2)
        elif cmd == 'off':
            self.turnOff(self.size(), x1, y1, x2, y2)
        elif cmd =='switch':
            self.switch(self.size(), x1, y1, x2, y2)
        else:
            print('Command not recognised')
       
    def count(self):
        count = 0
        for val in self:
            if val == "True":
                print('Found light on')
            count += 1
        return count
    
    def turnOn(self, N, x1, y1, x2, y2):
        for i in range (int(x1), int(x2)+1):
                for j in range(int(y1), int(y2)+1):
                    self.lights[i][j] = True
        print('Lights turned on')
                
    def turnOff(self, N, x1, y1, x2, y2):
        for i in range (int(x1), int(x2)+1):
                for j in range(int(y1), int(y2)+1):
                    self.lights[i][j] = False
        print('Lights turned off')