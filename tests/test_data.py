'''
Created on 1 Mar 2018

@author: Eimg
'''

from led_tester import led_lights
from led_tester import cli
from led_tester import utils

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 1000
    assert instructions[1] == 'turn off 660,55 through 986,197'