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
        
   # def apply(self, cmd):
    #    if cmd =='switch':  
     #       print('switch')
        #elif cmd == 'turn on':
        #elif cmd == 'turn off':
        
       
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