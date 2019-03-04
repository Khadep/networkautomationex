#!/usr/bin/env python
"""
Create three separate lists of IP addresses. The first list should be the IP addresses for the
Houston data center routers and should have over ten IP addresses in it including some duplicate IP
addresses.
The second list should be the Atlanta data center routers and should have at least eight IP
addresses including some that overlap with the Houston data center.
The third list should be the Chicago data center routers and should have at least eight IP
addresses. The Chicago IP addresses have some overlap with the IP addresses in both Houston
and in Atlanta
Convert each of these three lists to a set.
Using set operations, find the IP addresses that are duplicated between Houston and Atlanta.
Using set operations, find the IP addresses that are duplicated in all three sites.
Using set operations, find the IP addresses that are entirely unique in Chicago.
"""
from __future__ import print_function


Houston = []
Atlanta = []
Chicago = []
hou = str(range(0,11)).replace("[","").replace("]","").split(",")
atl = str(range(6,16)).replace("[","").replace("]","").split(",")
chi = str(range(9,19)).replace("[","").replace("]","").split(",")
first = '10.234.14.'


for octect in hou:
    thefull = octect.strip()
    full = first + thefull
    Houston.append(full)

for octect in atl:
    thefull2 = octect.strip()
    full = first + thefull2
    Atlanta.append(full)
    
for octect in chi:
    thefull3 = octect.strip()
    full = first + thefull3
    Chicago.append(full)


H = set(Houston)
A = set(Atlanta)
C = set(Chicago)

print (H & A)
print (H.intersection(A, C))
print (C.difference(A,H))