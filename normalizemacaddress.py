#!/usr/bin/env python

from __future__ import print_function, unicode_literals



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
            correctmac = separator.join(newmac)
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


