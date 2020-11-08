Mr. Robot
#########
:Author: David Boyd
:Date: 2020-11-07

Reconnassance
*************

.. code-block:: Bash

	nmap -A -p- -T5 $TM
	gobuster dir -u $TM -w                                           \
		/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt \
		-o gobuster-w-dirb-med.txt

Capture the Flag
****************

1. What is key 1?

	- 073403c8a58a1f80d943455fb30724b9

.. code-block:: Bash

	# check out gobuster's 200 status directories
	w3m $TM/robots
		> User-agent: *
		> fsocity.dic
		> key-1-of-3.txt
	curl $TM/key-1-of-3.txt -o key-1-of-3.txt

2. What is key 2?

	-

3. What is key 3?

	-





