#!/usr/bin/env python

from __future__ import print_function, unicode_literals

""" Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following
format:
01:23:45:67:89:AB
This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.
The function should have one parameter, the mac_address. It should return the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:
a:b:c:d:e:f
should be converted to:
0A:0B:0C:0D:0E:0F
Write several test cases for your function and verify it is working properly.
""" 
def normalizeMAC(Macaddress):
    Macaddress 

    try: 

        if Macaddress[4]==".":
            mac = Macaddress[1].upper().replace(".","")
            separator = ":"
            newmac = []
            while len(mac) > 0:
                entry = mac[:2]
                mac = mac[2:]
                newmac.append(entry)
            print (newmac)

        elif Macaddress[2] == '-':
            mac = Macaddress.upper().replace("-",":")
            print (mac)
        elif Macaddress[1] == ":" or "-" or ".":
            mac = Macaddress.upper().replace(".",":").replace("-",":")
            separator = "0"
            newmac = [""]
            while len(mac) > 0:
                entry = mac[:2]
                mac = mac[2:]
                newmac.append(entry)
            correctmac = separator.join(newmac)
            print (correctmac)

    except IndexError:
       print ("Completely off format, please try to put in a mac address")

normalizeMAC("a.b.c.d.e.f") 


