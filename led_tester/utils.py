'''
Created on 1 Mar 2018

@author: Eimg
'''
import urllib.request
import requests
import socket
import re
from turtledemo.sorting_animate import instructions1
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

def find_matches(instruction):
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    check = ' '.join(str(e) for e in instruction)
    if re.match(pat, check):
        return instruction
    else:
        k = []
        for i in instruction:
            str(i).replace(' ','')
            k.append(i)
        if k[0]=='turn' and k[4] == 'through':
            k[2:4] = [''.join(k[2:4])]
        elif k[0]=='switch' and k[3] == 'through':
            k[1:3] = [''.join(k[1:3])]
        elif k[0]=='turn' and k[3] == 'through':
            k[4:6] = [''.join(k[4:6])]
        elif k[0]=='switch' and k[2] == 'through':
            k[3:5] = [''.join(k[3:5])]
        return k

