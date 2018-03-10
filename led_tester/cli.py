# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
from led_tester.lights import LEDTester
from led_tester import utils
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for led_tester."""
    print("input", input) 
    N, instructions = utils.parseFile(input)
    ledTester = LEDTester(N)
    for instruction in instructions: 
        parsed_instruction = utils.find_matches(instruction)
        ledTester.apply(parsed_instruction)
    print('#occupied: ', ledTester.count()) 
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
    #main(input)
