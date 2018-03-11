==========
led_lights
==========


.. image:: https://img.shields.io/pypi/v/led_lights.svg
        :target: https://pypi.python.org/pypi/led_lights

.. image:: https://img.shields.io/travis/Eimg851/led_lights.svg
        :target: https://travis-ci.org/Eimg851/led_lights

.. image:: https://readthedocs.org/projects/led-lights/badge/?version=latest
        :target: https://led-lights.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




COMP30670 Assignment 3 - Program to monitor / control lights in science building
-------
The Science Centre is installing a new display board which is constructed from LED
lights.
The board is a square grid of LEDs which we control by sending commands to the unit
to turn on or off certain rectangular regions.
The L X L lights can be modelled as a 2 dimensional grid with L rows of lights and L
lights in each row and the LED's at each corner are (0, 0), (0, L - 1), (L - 1, L - 1)
and (L - 1, 0).
The lights are either on or off.
Your job is to test the lights. We test them by sending instructions to turn on, turn
off, or switch various inclusive ranges given as coordinate pairs. Each coordinate pair
represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through
2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
