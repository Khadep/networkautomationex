#!/usr/bin/env python

from  telnetlib import Telnet
from  netmiko import Netmiko

kp = Telnet('69.251.157.111', 5005)
response = kp.read_until("#", timeout=120)
command = reload

output = kp.send_command_timing(command, strip_prompt=False, strip_command=False)
if 'confirm' in output:
    # I don't confirm the file delete.
    output += kp.send_command_timing('n', strip_prompt=False, strip_command=False)
else:
    raise ValueError("Expected confirm message in output")
