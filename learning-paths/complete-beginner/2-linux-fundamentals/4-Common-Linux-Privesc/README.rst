Common Linux Privesc
####################
:Author: David Boyd
:Date: 2020-06-02

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

Python3
~~~~~~~

http.server    (import http.server)
	this module defines classes for implementing HTTP servers (Web servers).

	-m

Issue
~~~~~
:Issue: Python2 code is deprecated.
:Tricks: Use the **2to3** utility to convert Python2 prgms to Python3.
:Solution: The *SimpleHTTPServer* module has been merged into the
           *http.server* in Python 3.0

.. code-block :: Python3

	#
	python3 -m http.server 8000


.. code-block :: Python2

	python -m SimpleHTTPServer

