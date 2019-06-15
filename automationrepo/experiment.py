#!/usr/bin/env python
"""
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement
outside of your function (i.e. where you have your function calls).
Inside of pdb, experiment with:
1. Listing your code.
2. Using 'next' and 'step' to walk through your code. Make sure you understand the difference
   between the two.
3. Experiment with 'up' and 'down' to move up and down the code stack.
4. Use p <variable> to look at a variable.
5. Set a breakpoint and run your code to the breakpoint.
6. Use '!command' to change a variable (for example !new_mac = [])
"""
from __future__ import print_function, unicode_literals
import re
import pdb




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
            #pdb.set_trace()
            print (correctmac)

    except IndexError:
       print ("Completely off format, please try to put in a mac address")


normalizeMAC("8-8-8-8-9")
#pdb.run('normalizeMAC("a.b.c.d.e.f")')




