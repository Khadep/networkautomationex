#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import random

""" Randomly generates an IP address for a network.  """

def IPaddress(Basenetwork= '10.10.10.'):
    x = random.randint(1, 254)
    mask = '255.255.255.0'

    print ("Netork: " + Basenetwork + str(x) + " \n Mask: " + mask)    

IPaddress()

""" 
IPaddress()
IPaddress('192.168.0.') """
