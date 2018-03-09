'''
Created on 1 Mar 2018

@author: Eimg
'''
import urllib.request
help(urllib.request.urlopen)
import requests

def parseFile(input):
    if input.startswith('http'):
        uri = input
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        r = requests.get(uri).text
        N, instructions = None, []
        #print(r)
        #for line in r.readlines():
        #instructions = r.strip().split()
        #instructions.append(values)
        #values=('\n'.join(r.split('\n')))
        values = r.split('\n')
        N = int(values[0])
        for i in range(1,len(values)-1):
            instructions.append(values[i].strip().split())
        return N, instructions
        
        pass
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                values = line.strip().split()
                instructions.append(values)
        return N, instructions
    return
