'''
Created on 1 Mar 2018

@author: Eimg
'''
import urllib.request
import requests
import socket
socket.gethostbyname('localhost')

def parseFile(input):
    if input.startswith('http'):
        uri = input
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8').lower()
        r = requests.get(uri).text
        N,instructions = None, []
        values = r.split('\n')
        N = int(values[0])
        for i in range(1,len(values)-1):
            instructions.append(values[i].strip().split())
        print(instructions)
        return N, instructions
        
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline().split())
            for line in f.readlines():
                values = line.strip().split()
                instructions.append(values)
        return N, instructions
    return
