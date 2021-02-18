#!/usr/bin/env python3
# Copyright 2020 David Boyd, all rights reserved
# Program: review-requests.py
# Description:
#     +DESCR+
# Date: 2020-10-29
# Revised:

import requests

for i in range(0, 35):
    url = "http://10.10.128.7/rest/products/" + str(i) + "/reviews"
    webpage = requests.get(url)
    print("=================================================================")
    print(i, "[REVIEW] ", url, sep="")
    print("-------------------------------------------")
    # response.json() returns a JSON object of the result (if the result was
    # written in JSON format, if not it raises an error).
    print(webpage.json())
    print("\n")

print("END================================================================END")

