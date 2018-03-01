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
        
    def apply(self, cmd):
        if cmd =='switch':
        elif cmd == 'turn on':
        elif cmd == 'turn off':
            
    def count(self):
        count = 0
        for val in self:
            if val == "True"
            count += 1
        return count