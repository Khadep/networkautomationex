#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import re

"""
Read the 'show_ipv6_intf.txt' file.
From this file use Python regular expressions to extract the two IPv6 addresses.
The two relevant IPv6 addresses you need to extract are:
  IPv6 address:
    2001:11:2233::a1/24
    2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
Try to use re.DOTALL flag as part of your search. Your search pattern should not include any of
the literal characters in the IPv6 address.
From this, create a list of IPv6 addresses that includes only the above two addresses.
Print this list to the screen.
"""
with open("showipv6.txt") as ipv6:
    theipv6 = ipv6.read()

"""
 this = re.search(r"^  IPv6 address: .* (?P<ip1>\S+) .* with (?P<ip2>\S+) ", theipv6, flags=re.DOTALL)
    ip = this.groupdict('ip1')
    print ( ip )
"""
    
# Use re.DOTALL to have .* span newlines
match = re.search(r"IPv6 address:\s+(.*)\s+IPv6", theipv6, flags=re.DOTALL)
# Extract the matched pattern and strip any white space
ipv6_addresses = match.group(1).strip()
ipv6_list = ipv6_addresses.splitlines()
print (ipv6_list)
# Strip out [VALID] from the IPv6 address string
for i, address in enumerate(ipv6_list[:]):
    address = re.sub(r"\[VALID\]", "", address)
    ipv6_list[i] = address.strip()

print()
print('-' * 80)
print(ipv6_list)
print('-' * 80)
print()

