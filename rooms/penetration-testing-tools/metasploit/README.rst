Metasploit README
#################
:Author: David Boyd
:Date: 2020-10-11

Metasploitable Framework
	an open-src pentesting framework/tool
	[+] a collection of:
		- thoroughly tested exploits
		- auxiliary tools
		- exploitation tools
	[+] supports diff types of port scans from within the auxiliary modules
		- namp, Nessus, etc


Gettings Started
================
:Notes: WSL conflict with connecting to network bus --continue ops anyways

.. code-block:: Bash

	# Initialize and launch at the same time
	sudo msfdb init && msfconsole

.. code-block:: Bash

	# Start and Initialize the DB
	sudo msfdb init

	# Start wo showing the banner	// like starting the prgm without the logo
	-q								// this is dumb

	# Start metsploitable console	// (2) methods
	msfconsole						// msfconsole -q
	msfdb start						// 2nd method

	# Check status
	msfdb status
	msf5 > db_status			// WSL: [*] postgresql selected, no connection

########
Glossary
########
:msf: metasploit framework

module
	a piece of SW that the MSF uses to perform a task,
	such as exploiting, or scanning a target.
	Can be an exploit module, auxiliary module, or post-exploitation module.

##############
Common Modules
##############

auxiliary
	[+] most commonly used in *scanning and verification* of exploited machines
	[-] NOT the same as the actual exploitation

encoder
	allows us to modify the 'appearance' (encode) of our exploit
	[+] helps to avoid signature detection
	[+] common utilized in payload obfuscation

exploit
	holds all the exploit *code* we'll use
	[+] most common module utilized

payload
	used hand-in-hand with exploits
	this module contains *various bits of shellcode* we send to have executed
	following exploitation.

post
	provides *looting & pivoting* capabilities
	[+] most common activities "after" (post) exploitation

NOP (No OPeration --assembly language)
	used with buffer overflow and ROP attacks

########
Commands
########

?
	help menu

banner
	displays the motd/ascii art we see at the start of msfconsole
	[+] Easter Egg #purely4fun
	[+] can quiet the banner when starting msf by using '-q'

connect
	makes a quick connection with a host to verify that we can 'talk' to it.
	[+] a netcat-like function

db_nmap [option] [IP]
	runs nmap with options (db_nmap -T4 -sV IP.addr.0.1)
	[+] feeds nmaps results directly into our msfdb
	#see *hosts* *services* *vulns*

get
	view the value of single variables
	[+] see *set*

hosts
	display collected 'hosts' and their information (IP, MAC, name, OS, etc)
	[+] hosts are collected from feeding in results from scans
	#see *db_nmap* *services* *vulns*

info
	used to view information about either a specific module
	or just the active one we have selected

load
	used to load different modules
	[+] not every module is loaded in by default

save
	used to store the settings/active datastores from msf to a settings file.
	[+] this will save within your msf5 dir & can be undone by rm saved file.
	[+] used when loading previously set values		#session

search
	use for searchingn various modules
	[+] if (exploit=found) { use # } // use cmd with number saves write/path

services
	displays the 'host | port | protocol | state | info' in collected db
	[+] results are collected from scans
	#see *db_nmap* *hosts* *vulns*

sessions					// sessions -i <session id>
	lists established connections

set			// set [option] [value]
	used to change the value of a variable
	[+] 1/2 most used commands
	[+] see *get*

setg
	change the value of a global variable
	[+] msf supports the use of global variables
	[+] usefule when specifically focusing on a single box

spool
	set our console output to save to a file
	[+] useful to grep for different pieces of info output to the screen
	[+] commonly used with recording your screen for further review/providing
		evidence of any actions taken.

unset
	change the value of a var to null/no value

use
	used to select the found module we want to leverage as the *active module*

vulns
	displays record of **discovered vulnerabilities**.
	[+] allows us to leverage the msfdb quickly and powerfully
	#see *db_nmap* *hosts* *services*

###########
Meterpreter
###########
:URL: https://www.offensive-security.com/metasploit-unleashed/about-meterpreter

meterpreter
	is a payload within Metasploit Framework that provides control over an
	exploited target system, running as a DLL loaded inside of any process on a
	target machine.

	[2]an advanced, dynamically extensible *payload* that uses in-memory DLL
	   injection stagers and is extended over the network at runtime.

======================
Commands (meterpreter)
======================

migrate  <<pid> | -P <pid> | -N <name>> [-t timeout]
	Migrate the server to another process
	[+] Move/transfer ourselves into a process
	@pre: list processes: meterpreter > ps

#####
Notes
#####

payload
	refers to an exploit module.
	- 3 types:
		- singles
		- stagers
		- stages
	Ie) windows/shell_bind_tcp = 1 single payload, 0 stages
	Ie) windows/shell/bind_tcp = 1 stager (bind_tcp), 1 stage (shell)

postgresql
	a free and open-source *relational database management system* emphasizing
	extensibility and SQL compliance.
	Metasploit uses the 'postgresql' database.

###############
Troubleshooting
###############

WSL
===
:Issue: No network service running
:Issue: Database not connected
:STATUS: IN QUEUE
:REASON: WSL is not allowed to touch the Windows kernal
:Workaround: Dual-boot, VM, cloud (THM)

