#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import random

""" Create a function that randomly generates an IP address for a network. The default base network
should be '10.10.10.'. For simplicity the network will always be a /24.
You should be able to pass a different base network into your function as an argument.
Randomly pick a number between 1 and 254 for the last octet and return the full IP address.
You can use:
import random
random.randint(1, 254)
to randomly generate the last octet.
Call your function using no arguments.
Call your function using a positional argument
Call your function using a named argument.
For each function call print the returned IP address to the screen. """

def IPaddress(Basenetwork= '10.10.10.'):
    x = random.randint(1, 254)
    mask = '255.255.255.0'

    print ("Netork: " + Basenetwork + str(x) + " \n Mask: " + mask)    

IPaddress()

""" 
IPaddress()
IPaddress('192.168.0.') """