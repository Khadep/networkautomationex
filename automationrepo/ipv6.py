#!/usr/bin/env py
from __future__ import unicode_literals, print_function
import re


with open("show_ipv6_intf.txt") as Text:
    ipv6Text = Text.read()


khade = re.search(r'IPv6 address.*IPv6 subnet:' , ipv6Text, flags=re.DOTALL)
thelist = khade.group(0).split()
address = thelist[2]
address2 = thelist[4]
print ((address) + "\n" + (address2))
