from __future__ import unicode_literals, print_function
import re

with open("show_ipv6_intf.txt") as f:
    output = f.read()

# Use re.DOTALL to have .* span newlines
match = re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:", output, flags=re.DOTALL)
# Extract the matched pattern and strip any white space
ipv6_addresses = match.group(1).strip()
ipv6_list = ipv6_addresses.splitlines()
print (ipv6_list)
# Strip out [VALID] from the IPv6 address string
for i, address in enumerate(ipv6_list):
    address = re.sub(r"\[VALID\]", "", address)
    ipv6_list[i] = address.strip()

print()
print('-' * 80)
print(ipv6_list)
print('-' * 80)
print()