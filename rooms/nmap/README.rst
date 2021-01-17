Nmap - Walkthrough
##################
:Author: David Boyd
:Date: 2021-01-15
:Room: Nmap
:Version: 2
:Tasks: 15
:Learning Path: PenTest+
:Category: Penetration Testing Tools
:Prerequisites: https://tryhackme.com/room/introtonetworking
:Prerequisites: https://tryhackme.com/room/wireshark

[Task 1] Deploy
***************

1. Deploy the attached VM
=========================
:Answer: [No answer needed]

[Task 2] Introduction
*********************

1. What networking constructs are used to direct traffic to the right application on a server?
==============================================================================================
:Answer: Ports

2. How many of these are available on any network-enabled computer?
===================================================================
:Answer: 65536

3. [Research] How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)
=====================================================================================================================
:Answer: 1024

[Task 3] Nmap Switches
**********************
:Tip: man nmap

1. What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?
===========================================================================================
:Answer: -sS

2. Which switch would you use for a "UDP scan"?
===============================================
:Answer: -sU

3. If you wanted to detect which operating system the target is running on, which switch would you use?
=======================================================================================================
:Answer: -O

4. Nmap provides a switch to detect the version of the services running on the target. What is this switch?
===========================================================================================================
:Answer: -sV

5. The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?
=======================================================================================================================================
:Answer: -v

6. Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?  (Note: it's highly advisable to always use at least this option)
==================================================================================================================================================================================
:Answer: -vv

7. What switch would you use to save the nmap results in three major formats?
=============================================================================
:Answer: -oA

8. What switch would you use to save the nmap results in a "normal" format?
===========================================================================
:Answer: -oN

9. A very useful output format: how would you save results in a "grepable" format?
===================================================================================
:Answer: -oG

10. Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning. How would you activate this setting?
===========================================================================================================================================================================================================================================================================================================
:Answer: -A

11. Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors! How would you set the timing template to level 5?
===========================================================================================================================================================================================================================================
:Answer: -T5

12. How would you tell nmap to only scan port 80?
=================================================
:Answer: -p 80

13. How would you tell nmap to scan ports 1000-1500?
====================================================
:Answer: -p 1000-1500

14. How would you tell nmap to scan all ports?
==============================================
:Answer: -p-

15. How would you activate a script from the nmap scripting library?
====================================================================
:Answer: --script

16. How would you activate all of the scripts in the "vuln" category?
=====================================================================
:Answer: --script="vuln"
:Alt Method: --script "vuln"

[Task 4] [Scan Types] Overview
******************************

1. Read the Scan Types Introduction.
====================================
:Answer: [No answer needed]

[Task 5] [Scan Types] TCP Connect Scans
***************************************

TCP Connect scans use the ``-sT`` switch to perform the *TCP three-way
handshake*.

TCP three-way handshake
	consists of three stages.  **First**, the connecting terminal ($AM) sends a
	TCP request to the $TM with the *SYN flag* set.  **Secondly**, the $TM
	*acknowledges* this packet with a tCP response containing the *SYN flag*,
	as well as the *ACK flag*.  #SYN/ACK.  **Thirdly**, our $AM completes the
	handshake by sending a tCP request with the *ACK flag* set.

Nmap uses the TCP three-way handshake to determine port states #RFC793.

If the port is **closed**, then the $TM will respond with a TCP packet with the
*RST flag* set.  Note: $AM must 1st send a TCP pkt with its SYN flag set.

If the port is **filtered**, then the $AM receives *NO RESPONSE*.  This
indicates that the port is being protected by a firewall and the port's state
is undetermined.  Note: Many FWs are configured to simply *drop* incoming pkts.

.. code-block:: bash

	# config FW to repond w/ an RST TCP pkt using IPtables
	iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset

1. Which RFC defines the appropriate behaviour for the TCP protocol?
====================================================================
:Answer: RFC 793

2. If a port is closed, which flag should the server send back to indicate this?
================================================================================
:Answer: RST

[Task 6] [Scan Types] SYN Scans
*******************************

SYN scans, aka, "Half-open" scans, "Stealth" scans.

If Nmap is ran with sudo, then default scans are SYN scans; else default scans
are TCP Connect scans.

Advantages for 黑客們:

	- bypass *older IDS*, not too common anymore, though
	- often not logged by applications listening on open ports
	- significantly faster than std TCP Connect scans

Disadvantages:

	- require sudo privileges
	- unstable services can be brought down by SYN scans (ICS, SCADA, LPC, etc)

1. There are two other names for a SYN scan, what are they?
===========================================================
:Answer: half-open, stealth

2. Can Nmap use a SYN scan without Sudo permissions (Y/N)?)
===========================================================
:Answer: N

[Task 7] [Scan Types] UDP Scans
*******************************

Closed UDP ports are determined by receiving an *ICMP (ping)* pkt containing a
message that the port is *unreachable*.

Open|filtered UDP ports are determined by receiving no response.

Disadvantages:

	- slower cmp to TCP Connect scans (>=2 ACK TCP pkts to determine response
	  as none) Note: 1000 port UDP scan >=20 minutes

Therefore, when using UDP scans, use ``--top-ports <number>``.
For example, ``nmap -sU --top-ports 20 <target>``.

1. If a UDP port doesn't respond to an Nmap scan, what will it be marked as?
============================================================================
:Answer: open|filtered

2. When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?""
=============================================================================================================================================
:Answer: ICMP

[Task 8] [Scan Types] NULL, FIN, and XMAS
*****************************************
:NULL, FIN, and XMAS: Stealthier methods for FW evasion
:closed ports: *RST* flag
:open|filtered ports: *no response*
:filtered port: *ICMP unreachable* packet
:Warning: Windows, ~Cisco dev, etc may respond with a *RST* packet if receiving a malformed packet.

NULL
	``-sN`` are when the TCP request is sent with *no flags* set at all.  The
	$TM responds with a *RST* flag if closed.

FIN
	``-sF`` are when the TCP request is sent with a *FIN* flag set.  The $TM
	responds with a *RST* if closed.

XMAS
	``-sX`` are when the TCP request is sent with *PSH*, *URG*, and *FIN* flags
	set... giving it the appearance of a blinking christmas tree when viewed as
	a packet capture in Wireshark.  The $TM responds with a *RST* for closed
	ports.

1. Which of the three shown scan types uses the URG flag?
=========================================================
:Answer: XMAS

2. Why are NULL, FIN and Xmas scans generally used?
===================================================
:Answer: firewall evasion

3. Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?
=====================================================================================
:Answer: Microsoft Windows

[Task 9] [Scan Types] ICMP Network Scanning
*******************************************

1. How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)
==================================================================================================================
:Answer: nmap -sc 172.16.0.0./16

[Task 10] [NSE Scripts] Overview
********************************
:NSE Categories: https://nmap.org/book/nse-usage.html

Some NSE Categories:

	- safe: won't affect the target
	- intrusive: not safe: liekly to affect the target
	- vuln: scan for vulnerabilities
	- exploit: attempt to exploit a vulnerability
	- auth: attempt to bypass authentication for running services

		- ie) anonymous FTP server log in

	- brute: attempt to bruteforce credentials for running services
	- discovery: attempt to query running services for further information about the newtork

		- ie) query an SNMP server

1. What language are NSE scripts written in?
============================================
:Answer: Lua

2. Which category of scripts would be a very bad idea to run in a production environment?
=========================================================================================
:Answer: intrusive

[Task 11] [NSE Scripts] Working with the NSE
********************************************
:Scripts List: https://nmap.org/nsedoc/
:Note: Only scripts which target an active service will be activated

.. code-block:: bash

	# Run a script based off its category
	nmap --script=vuln $TM							# --script=<vuln|safe|etc>

	# Run a specific script
	nmap --script=http-fileupload-exploiter			# --script=<script-name>

	# Run multiple scripts
	nmap --script=smb-enum=users,smb-enum-shares	# IFS=','

	# Run script with required arguments			# use --script-args <x,y>
													# <script-name>.<argument>
	nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'

1. What optional argument can the ftp-anon.nse script take?
===========================================================
:Answer: maxlist

[Task 12] [NSE Scripts] Searching for Scripts
*********************************************

Scripts Locations:

	1. [Linux] https://nmap.org/nsedoc/
	2. [Linux] ``/usr/share/nmap/scripts``
	3. [Windows] C:\Program Files (x86)\Nmap\scripts

Searching for scripts:

.. code-block:: bash

	# access the scripts.db file itself
	cat /usr/share/nmap/scripts/script.db

	# grep service|category
	grep 'ftp\|safe' /usr/share/nmap/scripts/script.db

	# ls filename
	ls -l /usr/share/nmap/scripts/*ftp*

Updating/Installing Scripts:

.. code-block:: bash

	# Update Nmap
	sudo apt update nmap

	# Manually install script
	sudo wget -O /usr/share/nmap/scripts/<script-name> https://svn.nmap.org/nmap/scripts/<script-name>.nse

	# Update NSE database (script.db)
	nmap --script-updatedb

1. Search for "smb" scripts in the /usr/share/nmap/scripts/ directory using either of the demonstrated methods.  What is the filename of the script which determines the underlying OS of the SMB server?
=========================================================================================================================================================================================================
:Answer: smb-os-discovery.nse

[Walkthrough]
-------------

.. code-block:: bash

	ls -l /usr/share/nmap/scripts/*smb*os*

2. Read through this script. What does it depend on?
====================================================
:Answer: smb-brute

Hint:

	- Look for `dependencies = {}` in the Lua script.

[Task 13] Firewall Evasion
**************************
:FW Evasion: https://nmap.org/book/man-bypass-firewalls-ids.html
:Note: If you're already on the the LAN, use Nmap's ARP requests to determine host activity.

You typical Windows host will, with its default FW, *block all ICMP packets*.
Therefore, Nmap will register a host with its FW configuration as dead and not
bother scanning at all.  Therefore, we use the ``-Pn`` option, which tells Nmap
to not bother pinging the host before scanning it.  The disadvantage to this
method is that if the host doesn't actually exist, then we're wasting a lot of
time scanning every port!

Some FW evasion options:

	- ``-f``: Used to fragment the packets; making them less likely that the
		packets will be detected by a FW/IDS.
	- ``--mtu <number>``: same as ``-f``, but providing more control over the
		MTU size for the packets sent.  *Must be a multiple of 8.*
	- ``--scan-delay <time>ms``: used to add a delay b/t packets sent.  Useful
		if the network is unstable, but also for evading any time-based FW/IDS
		triggers.
	- ``--badsum``: used to generate an invalid checksum for packets.  Any real
		TCP/IP stack would drop this packet, however, FWs may potentially
		respond automatically, wihtout bothering to check the checksum of the
		packet.  Useful for determining the presence of a FW/IDS.

1. Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch?
============================================================================================================
:Answer: ICMP

2. [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?])
================================================================================================================
:Answer: --data-length

[Task 14] Practical
*******************

1. Does the target (10.10.253.86)respond to ICMP (ping) requests (Y/N)?
=======================================================================
:Answer: N

[Walkthrough]
-------------

[Windows] Zenmap
^^^^^^^^^^^^^^^^

.. code-block:: Zenmap

	nmap -sn $TM
	  > Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-15 23:46 Central Standard Time
	  > Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
	  > Nmap done: 1 IP address (0 hosts up) scanned in 4.61 seconds))


[WSL2] Kali
^^^^^^^^^^^
:1-ERROR: ``-sn`` consists of an ICMP echo request, yet non-sudo returns host is up.
:1-SOLUTION: use ``-Pn`` to bypass ICMP echo request

.. code-block:: bash

	# perform host discovery while bypassing ICMP echo request
	nmap -Pn -T5 -vv $TM
	  > Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
	  > ...
	  > Scanning 10.10.149.100 [1000 ports]
	  > Discovered open port 135/tcp on 10.10.149.100
	  > Discovered open port 21/tcp on 10.10.149.100
	  > Discovered open port 53/tcp on 10.10.149.100
	  > Discovered open port 3389/tcp on 10.10.149.100
	  > Discovered open port 80/tcp on 10.10.149.100
	  > ...
	  > Nmap done: 1 IP address (1 host up) scanned in 17.78 seconds

.. code-block:: bash

	# 1-ERROR (false negative)
	ping -c5 $TM
	  > --- 10.10.254.230 ping statistics ---
	  > 5 packets transmitted, 0 received, 100% packet loss, time 4140ms

	# 1-ERROR: (true positive), ?=non-sudo is correct, but sudo isn't, why?
	nmap -sn $TM
	  > Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-15 23:18 CST
	  > Nmap scan report for 10.10.254.230
	  > Host is up (0.24s latency).
	  > Nmap done: 1 IP address (1 host up) scanned in 1.38 seconds

	# 1-ERROR (false negative)
	sudo nmap -sn $TM
	  > Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-15 23:18 CST
	  > Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
	  > Nmap done: 1 IP address (0 hosts up) scanned in 3.03 seconds

2. Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?
================================================================================================================
:Answer: 999

[Walkthrough]
-------------
:Notes: use ``-Pn``

[Windows] Zenmap
^^^^^^^^^^^^^^^^

.. code-block:: Zenmap

	nmap -Pn -sX -p 1-999 -vv $TM
	  > Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-15 23:51 Central Standard Time
	  > Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
	  > Initiating Parallel DNS resolution of 1 host. at 23:51
	  > Completed Parallel DNS resolution of 1 host. at 23:51, 0.04s elapsed
	  > Initiating XMAS Scan at 23:51
	  > Scanning 10.10.254.230 [999 ports]
	  > XMAS Scan Timing: About 15.52% done; ETC: 23:55 (0:02:49 remaining)
	  > XMAS Scan Timing: About 29.78% done; ETC: 23:55 (0:02:24 remaining)
	  > XMAS Scan Timing: About 45.05% done; ETC: 23:55 (0:01:51 remaining)
	  > XMAS Scan Timing: About 59.56% done; ETC: 23:55 (0:01:22 remaining)
	  > XMAS Scan Timing: About 74.17% done; ETC: 23:55 (0:00:53 remaining)
	  > Completed XMAS Scan at 23:55, 204.03s elapsed (999 total ports)
	  > Nmap scan report for 10.10.254.230
	  > Host is up, received user-set.
	  > All 999 scanned ports on 10.10.254.230 are open|filtered because of 999 no-responses
	  > Read data files from: C:\Program Files (x86)\Nmap
	  > Nmap done: 1 IP address (1 host up) scanned in 205.59 seconds
	  > Raw packets sent: 1998 (79.920KB) | Rcvd: 0 (0B)

3. There is a reason given for this -- what is it?  Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!
===========================================================================================================================================================================================
:Answer: no responses

4. Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?
=======================================================================================================
:Answer: 5

[Walkthrough]
-------------

WSL2
^^^^

.. code-block:: bash

	nmap -Pn -p 1-5000 -T5 -vv $TM
	  > Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.
	  > Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-16 17:55 CST
	  > Initiating Parallel DNS resolution of 1 host. at 17:55
	  > Completed Parallel DNS resolution of 1 host. at 17:55, 1.16s elapsed
	  > Initiating Connect Scan at 17:55
	  > Scanning 10.10.149.100 [5000 ports]
	  > Discovered open port 21/tcp on 10.10.149.100
	  > Discovered open port 3389/tcp on 10.10.149.100
	  > Discovered open port 53/tcp on 10.10.149.100
	  > Discovered open port 135/tcp on 10.10.149.100
	  > Discovered open port 80/tcp on 10.10.149.100
	  > Completed Connect Scan at 17:56, 60.15s elapsed (5000 total ports)
	  > Nmap scan report for 10.10.149.100
	  > Host is up, received user-set (0.21s latency).
	  > Scanned at 2021-01-16 17:55:56 CST for 60s
	  > Not shown: 4995 filtered ports
	  > Reason: 4995 no-responses
	  > PORT     STATE SERVICE       REASON
	  > 21/tcp   open  ftp           syn-ack
	  > 53/tcp   open  domain        syn-ack
	  > 80/tcp   open  http          syn-ack
	  > 135/tcp  open  msrpc         syn-ack
	  > 3389/tcp open  ms-wbt-server syn-ack
	  > Read data files from: /usr/bin/../share/nmap
	  > Nmap done: 1 IP address (1 host up) scanned in 61.40 seconds

5. Open Wireshark (see Cryillic's Wireshark Room for instructions) and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on.
==================================================================================================================================================================================================
:Answer: [No answer needed]

6. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)
==============================================================================================================
:Answer: N

[Walkthrough]
-------------

WSL2
^^^^

.. code-block:: bash

	grep 'ftp\|anon' /usr/share/nmap/scripts/script.db
	  > Entry { filename = "ftp-anon.nse", catergores = { "auth", "default", "safe", } }
	  > ...
	nmap -Pn -p21 --script=ftp=anon.nse -vv $TM
	  > Starting Nmap 7.91 ( https://nmap.org ) at 2021-01-16 18:02 CST
	  > NSE: Loaded 1 scripts for scanning.
	  > NSE: Script Pre-scanning.
	  > NSE: Starting runlevel 1 (of 1) scan.
	  > ...
	  > PORT   STATE SERVICE REASON
	  > 21/tcp open  ftp     syn-ack
	  > | ftp-anon: Anonymous FTP login allowed (FTP code 230)
	  > | _Can't get directory listing: TIMEOUT
	  > ...
	  > Nmap done: 1 IP address (1 host up) scanned in 33.18 seconds

[Task 15] Conclusion
********************

1. Read the conclusion.
=======================
:Answer: [No answer needed]

