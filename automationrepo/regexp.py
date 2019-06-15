#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import re


show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X
5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

khade = re.search(r"^Cisco (?P<model>\S+) .* with (?P<memory>\S+) " , show_version, flags=re.M)
model = khade.groupdict()['model']
memory = khade.groupdict()['memory']

print(model)
print(memory)