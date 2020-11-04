README
#######
:Author: David Boyd
:Date: 2020-10-18

gobuster
========
:URL: https://redteamtutorials.com/2018/11/19/gobuster-cheatsheet/

gobuster
	a tool used to brute-force URIs
	including directories and files
	as well as DNS subdomains

Commands
========

.. code-block:: Bash
	# Basic help menu
	gobuster -h

	# Command help menu (example)
	gobuster dir --help

+------+---------------------------------------+-----------------------+
| Mode | Description                           | Commonly Used With... |
+======+=======================================+=======================+
| dir  | Specify directory/file to brute force | -u -w                 |
+------+---------------------------------------+-----------------------+
| dns  | Specify DNS bruteforcing mode         |                       |
+------+---------------------------------------+-----------------------+

+-------+-----+--------------------------------------------+
| Mode  | Cmd | Description                                |
+=======+=====+============================================+
| <any> | -t  | sets the threads (default=10); set to 40   |
+-------+-----+--------------------------------------------+
| <any> | -x  | sets the '.extensions' to be used          |
+-------+-----+--------------------------------------------+
| <any> | -w  | set the wordlist to be used                |
+-------+-----+--------------------------------------------+
| dir   | -U  | sets the Username for basic authentication |
+-------+-----+--------------------------------------------+
| dir   | -P  | sets the Password for basic authentication |
+-------+-----+--------------------------------------------+
| dir   | -s  | skip the SSL Certification verification    |
+-------+-----+--------------------------------------------+
| dir   | -a  | Specify a User-Agent                       |
+-------+-----+--------------------------------------------+

*REFER to the gobuster cheatsheet for more*

Flags
=====

	.. code-block:: Bash

	# Find the hidden directory
	gobuster dir -u $TM -w \
	/usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-small.txt -t 40

	# Find the hidden file with the extension xxa
	gobuster dir -u $TM -w \
	/usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-small.txt \
	-t 40 -x xxa

Status Codes
============
:301: Moved Permanently

