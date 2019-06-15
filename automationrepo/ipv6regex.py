#!/usr/bin/env py
from __future__ import unicode_literals, print_function
import re


"""
Read the 'show_ipv6_intf.txt' file.
From this file use Python regular expressions to extract the two IPv6 addresses.
The two relevant IPv6 addresses you need to extract are:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of
the literal characters in the IPv6 address.
From this, create a list of IPv6 addresses that includes only the above two addresses.
Print this list to the screen.
"""

with open("show_ipv6_intf.txt") as Text:
    ipv6Text = Text.read()


khade = re.search(r'IPv6 address.*\n.*\n.*\n' , ipv6Text, flags=re.M)
thelist = khade.group(0).split()
address = thelist[2]
address2 = thelist[4]
print (address)
print (address2)



#print (FirstIP1)
#print (secondIP1)
