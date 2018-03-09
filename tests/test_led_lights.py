#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_lights` package."""
import sys
from turtledemo.sorting_animate import instructions1
sys.path.append('.')
import pytest

from click.testing import CliRunner

from led_tester import cli
from led_tester import utils
from led_tester.lights import LEDTester

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests
    return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    
def test_reading_from_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    print(instructions)
    assert N == 10
    assert instructions[0] == ['turn', 'on', '0,0', 'through', '9,9']
    
def test_parsing_from_http_file():
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 1000
    assert instructions[0] == ['turn', 'off', '660,55', 'through', '986,197']
    
def test_light_grid_local_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    led_test1 = LEDTester(N)
    assert led_test1.size() == 100
    
def test_light_grid_http_file():
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    led_test2 = LEDTester(N)
    assert led_test2.size() == 1000000
    
def test_apply_lights_on():
    instructions = [['turn', 'on', '2,2', 'through', '4,4']]
    led_test = LEDTester(10)
    assert led_test.lights[2][2] == False
    for instruction in instructions:
        led_test.apply(instruction)
    assert led_test.lights[2][2] == True
    assert led_test.lights[1][1] == False
    
def test_apply_lights_off():
    instructions = [['turn', 'on', '2,2', 'through', '4,4'], ['turn', 'off', '2,2', 'through', '3,3']]
    led_test = LEDTester(10)
    assert led_test.lights[2][2] == False
    for instruction in instructions:
        led_test.apply(instruction)
    assert led_test.lights[2][2] == False
    assert led_test.lights[4][4] == True
    
def test_turnOn():
    led_test= LEDTester(10)
    assert led_test.lights[2][2] == False
    assert led_test.lights[2][3]==False
    assert led_test.lights[3][4]==False
    assert led_test.lights[4][4]==False
    led_test.turnOn(led_test.size(), 2, 2, 4, 4)
    assert led_test.lights[2][2] ==True
    assert led_test.lights[2][3]==True
    assert led_test.lights[3][4]==True
    assert led_test.lights[4][4]==True
    assert led_test.lights[1][1] == False
    
def test_turnOff():
    led_test= LEDTester(10)
    assert led_test.lights[2][2] == False
    led_test.turnOn(led_test.size(), 2, 2, 4, 4)
    assert led_test.lights[2][2]==True
    assert led_test.lights[2][3]==True
    assert led_test.lights[3][4]==True
    assert led_test.lights[4][4]==True
    assert led_test.lights[1][1]==False
    led_test.turnOff(led_test.size(), 2, 2, 4, 4)
    assert led_test.lights[2][2]==False
    assert led_test.lights[2][3]==False
    assert led_test.lights[3][4]==False
    assert led_test.lights[4][4]==False
    
def test_swtich():
    led_test= LEDTester(10)
    assert led_test.lights[2][2]==False
    assert led_test.lights[2][3]==False
    assert led_test.lights[3][4]==False
    assert led_test.lights[4][4]==False
    led_test.switch(led_test.size(), 2, 2, 4, 4)
    assert led_test.lights[2][2]==True
    assert led_test.lights[2][3]==True
    assert led_test.lights[3][4]==True
    assert led_test.lights[4][4]==True
    led_test.switch(led_test.size(), 2, 2, 4, 4)
    assert led_test.lights[2][2]==False
    assert led_test.lights[2][3]==False
    assert led_test.lights[3][4]==False
    assert led_test.lights[4][4]==False
    
def test_count():
    led_test= LEDTester(10)
    assert led_test.count() == 0
    led_test.turnOn(led_test.size(), 2, 2, 4, 4)
    assert led_test.count() == 9
    
       
    