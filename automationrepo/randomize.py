#!/usr/bin/env python
"""
Create a function that randomly generates an IP address for a network. The default base network
should be '10.10.10.'. For simplicity the network will always be a /24.
You should be able to pass a different base network into your function as an argument.
Randomly pick a number between 1 and 254 for the last octet and return the full IP address.
You can use:
import random
random.randint(1, 254)
to randomly generate the last octet.
Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.
For each function call print the returned IP address to the screen.
"""
from __future__ import print_function, unicode_literals
import random

def Randomip(baseNetwork = "10.10.10."):
    x = random.randint(0,255)
    print ((baseNetwork) + str(x))


Randomip()
Randomip("4.2.2.")
Randomip(baseNetwork="192.168.1.")
