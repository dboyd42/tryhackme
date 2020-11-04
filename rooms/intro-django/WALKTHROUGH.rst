Walkthrough
###########
:Author: David Boyd
:Date: 2020-10-31

============
Introduction
============

Now it's time for a small CTF!

It might take around ~3 minutes for the machine to boot properly.

Fix the error and retrieve all the flags! (Use knowledge from previous units)

Username: django-admin
Password: roottoor1212

===================
Questions & Answers
===================

Quick Way
---------

The quickest and easiest way to to hack this box is by not following the rule.
SSH in with the admin credentials.

.. code-block:: bash

	# Get admin flag
	strings db.sqlite3 | grep THM{

	# Get user flag and hidden flag
	grep -rnw /home/ -e "THM" 2>/dev/null

The Approach
------------

Perform the appropriate reconnaisance on the box. To find ports 22,8000 open.

.. code-block:: bash

	nmap -A -T5 $TM
	# [Results]
	> 22/open/tcp//ssh//OpenSSH
	> 8000/open/tcp//http-alt//WSGIServer|0.2 CPython|3.6.9/

SSH with the previously provided credentials.  Then find out who you are and
what privleges you have.

.. code-block:: bash

	whoami
	# list all the sudoers
	getent group sudo
	# check your sudoer priviliges
	sudo -l

Okay, cool!  So, you're already a sudoer! (hence why the quick and dirty way of
finding the answers works!)

#1 Admin panel flag?
--------------------

You're starting directory is in the django_admin's home directory.  Cool, so
let's check out what files lay in waste.

.. code-block:: bash

	# 'tree' doesn't work :(
	tree
	ls
	ls messagebox

	# 'sqlite3' doesn't work :(
	sqlite3
	strings db.sqlite3 | grep THM{

	# -OR- (what I did originally)
	vi db.sqlite3
	/THM

	# You'll also find StrangeFox's URL to his hashed password
	https://pastebin.com/nmKt4BSf

:ANS: THM{DjanGO_Adm1n}

#2 User flag?
-------------

From the previously given link, go to crackstation.net and crack StrangeFox's
password.  From there, just su or SSH using StrangeFox's password.

.. code-block:: bash

	# switch user
	su StrangeFox
	WildNature

	# display the file in home dir
	cat user.txt

	# NOTE: The hacky way (as django_admin... you already have access!!!)
	cat /home/StrangeFox/user.txt

:ANS: THM{SSH_gUy_101}

#3 Hidden flag?
---------------

.. code-block:: bash

	# View the user's history --a lot of these boxes don't clear their history
	history

	# Check out that view.html
	grep view.html THM

