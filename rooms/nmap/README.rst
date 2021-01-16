Nmap - Walkthrough
##################
:Author: David Boyd
:Date: 2021-01-15
:Location: Learning-Paths/Pentest+/Penetration-Testing-Tools/Nmap
:Room Version: 2
:Tasks: 15

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

TCP Connect scans use the `-sT` switch to perform the *TCP three-way
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
	- unstable services can be brought down by SYN scans

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

Therefore, when using UDP scans, use `--top-ports <number>`.  For example,
`nmap -sU --top-ports 20 <target>`.

1. If a UDP port doesn't respond to an Nmap scan, what will it be marked as?
============================================================================
:Answer: open|filtered

2. When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?""
=============================================================================================================================================
:Answer: ICMP

[Task 8] [Scan Types] NULL, FIN, and XMAS
*****************************************

1. Which of the three shown scan types uses the URG flag?
=========================================================
:Answer:

2. Why are NULL, FIN and Xmas scans generally used?
===================================================
:Answer:

3. Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?
=====================================================================================
:Answer:

[Task 9] [Scan Types] ICMP Network Scanning
*******************************************

1. How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)
==================================================================================================================
:Answer:

[Task 10] [NSE Scripts] Overview
********************************

1. What language are NSE scripts written in?
============================================
:Answer:

2. Which category of scripts would be a very bad idea to run in a production environment?
=========================================================================================
:Answer:

[Task 11] [NSE Scripts] Working with the NSE
********************************************

1. What optional argument can the ftp-anon.nse script take?
===========================================================
:Answer:

[Task 12] [NSE Scripts] Searching for Scripts
*********************************************

1. Search for "smb" scripts in the /usr/share/nmap/scripts/ directory using either of the demonstrated methods.  What is the filename of the script which determines the underlying OS of the SMB server?
=========================================================================================================================================================================================================
:Answer:

2. Read through this script. What does it depend on?
====================================================
:Answer:

[Task 13] Firewall Evasion
**************************

1. Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch?
============================================================================================================
:Answer:

2. [Research] Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?])
================================================================================================================
:Answer:

[Task 14] Practical
*******************

1. Does the target (10.10.253.86)respond to ICMP (ping) requests (Y/N)?
=======================================================================
:Answer:

2. Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?
================================================================================================================
:Answer:

3. There is a reason given for this -- what is it?  Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!
===========================================================================================================================================================================================
:Answer:

4. Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?
=======================================================================================================
:Answer:

5. Open Wireshark (see Cryillic's Wireshark Room for instructions) and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on.
==================================================================================================================================================================================================
:Answer:

6. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)
==============================================================================================================
:Answer:

[Task 15] Conclusion
********************

1. Read the conclusion.
=======================
:Answer: [No answer needed]

