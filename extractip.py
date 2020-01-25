#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import re

"""
Read the 'show_ipv6_intf.txt' file.

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

