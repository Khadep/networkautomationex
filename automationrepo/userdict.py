#!/usr/bin/env python
"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""
from __future__ import unicode_literals, print_function

DS = { 'ip_addr' : '10.234.12.20', 'vendor' : 'cisco', 'username' : 'khade', 'password' : 'whoknows'}

print (DS['ip_addr'])

if DS['vendor'].lower() == 'cisco':
    DS['platform'] = 'ios'
elif DS['vendor'].lower() == "juniper":
    DS['platform'] = 'junos'
elif DS['vendor'].lower() == 'Dell':
    DS['platform'] = 'os6'


bgp_fields = { 'bgp_as': '122', 'peer_as' : '174', 'peer_ip' : '192.168.50.5'}

DS.update(bgp_fields)





for i, x in DS.items():
    print (i)

print ("*" * 50 )
for i, x in DS.items():   
    print (i, " --->", x)