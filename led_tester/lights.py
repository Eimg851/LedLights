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
            
        x,y =[],[]
        x = start.split(',')
        y = end.split(',')
        
        start_row = x[0]
        end_row = y[0]
        start_col = x[1]
        end_col = y[1]
        print(start_row, end_row, start_col, end_col)
        
        if cmd == 'switch':
            for i in range (int(start_row), int(end_row)):
                for j in range(int(start_col), int(end_col)):
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    else:
                        self.lights[i][j] = True
        elif cmd == 'on':
            for i in range (int(start_row), int(end_row)):
                for j in range(int(start_col), int(end_col)):
                    self.lights[i][j] = True
        elif cmd == 'turn off':
            for i in range (int(start_row), int(end_row)):
                for j in range(int(start_col), int(end_col)):
                    self.lights[i][j] = False
       
    #def count(self):
     #   count = 0
      #  for val in self:
       #     if val == "True":
        #        print('Found light on')
         #   count += 1
        #return count
    
   # def turnOn(self):
    #    for val in self:
     #       if val == 'False':
     #           val = ['True']
      #      print('Light turned on')
                
    #def turnOff(self):
     #   for val in self:
      #      if val == 'True':
       #         val = ['False']
        #    print('Light turned off')