BurpSuite
##########
:Author: David Boyd
:Date: 2020-10-10
:Room: BurpSuite
:Tasks: 14
:Learning Path: PenTest+
:Category: Penetration Testing Tools
:Prerequsites: https://tryhackme.com/room/webfundamentals

Documents
*********

xplatform-shoretened.txt
========================
:Summary: a shortened list of fuzzdb SQLi platform detection list
:full list: https://github.com/fuzzdb-project/fuzzdb/blocb/master/attack/sql-injection/detect/xplatform.txt
:Used in: Intruder (Task9)

[Task 1] Intro
**************

1. Read the overview and continue on into installation!
=======================================================
:Answer: [No answer needed]

Setting Up
**********
:Req: Burpsuite, Web Browser (Firefox)

1.	Installations

	- Install Burpsuite Community Edition (go online)
	- Install browser proxy extension (Firefox: Foxy Proxy)

2.	Setup Web Browser Proxy to proxy Burpsuite

	- Foxy Proxy > Options > Add
		- Title:burp
		- Proxy Type:HTTP
		- Proxy IP address:127.0.0.1
		- Port:8080
	- Save

2.	Install Burpsuite CA Certificate on Web Browser (Firefox)

	- Web Browser > Proxy Extension > burp (enable)
	- Web Browser > http://localhost:8080 (127.0.0.1:8080)
	- Download CA Certificate
	- Menu > Preferences > Find in Preferences: cert
	- View Certificates > Import > cacert.der
	- [Checkbox] Trust the CA ti identify web sites
	- [Checkbox] Trust the CA ti identify email users

Burpsuite Features
==================

Terms
-----

payload
	items form our word list

set of payloads
	one wordlist

Intruder
--------

Allows repeat testing nce a 'proof of conecpt' has been established.

**Common Usage:**

	- enumerating:
		- identifers (usernames, etc)
		- cycling thorugh predicatble session/password recovery tokens
		- attempting simple password guessing
	- harvesting (through grepping our responses)
		- data from profiles
		- other pages of interest
	- fuzzing for vulnerabilities
		- SQL injection
		- XSS
		- file path traversal

**Attack Type:**

positions = fields (username, password, whatever, etc.)
payload = item in wordlist
set of payloads = one wordlist

Sniper
	The most popular attack type,
	this cycles through out selected positions, putting the next available
	payload (items from our wordlist) in each position in turn.
	This uses only one set of payloads (one wordlist)


Battering ram
	Similar to Sniper,
	Battering Ram uses only one set of payloads.  Unlike Sniper,
	Battering ram puts every payload into *every selected position*.
	Think about how a bettering ram makes contact across a large surface with a
	single surface, hence the name Battering ram for this attack type.

Pitchfork
	Allows us to use *multiple payload sets* (one per position selected)
	and iterate through both paylod sets *simulataneously*.
	For example, if we selected two positions
		(say a username field and a password field),
	we can provide a username and password payload list.
	Intruder will then cycle through the combinations of usernames & passwords,
	resulting in a total number of combinations equalling the
	*smallest payload* set provided.

Cluster bomb
	Allows us to use multiple payload sets (one per position selected) and
	iterate through all combinations of the payload lists we provide.
	For example, if we selected two poistions
		(say a username field and a password field),
	we can provide a username and password payload list.
	Intruder will then cycle through the combinations of usernames & passwords,
	resulting in a total number of combinations equalling
	*usernames x passwords*.
	:NOTE: Can get lengthy if you're using the community edition of Burp.


positions = fields (username, password, whatever, etc.)
payload = item in wordlist
set of payloads = one wordlist

+---------------+-----------------------------+-----------------------------------------------+
| Attack Type   | Payload (nSets/position)    | Iteration (set/position)                      |
+===============+=============================+===============================================+
| Sniper        | single (payload++/position) | iterate next payload in each position in turn |
+---------------+-----------------------------+-----------------------------------------------+
| Battering ram | single (one/position)       | iterate simulataneiously                      |
+---------------+-----------------------------+-----------------------------------------------+
| Pitchfork     | multi (multi/position)      | iterate simulataneiously                      |
+---------------+-----------------------------+-----------------------------------------------+
| Cluster bomb  | multi (one/position)        | iterate all possible combos                   |
+---------------+-----------------------------+-----------------------------------------------+

Poxy
----
:Intercept: On|Off: Decide if proxy will intercept E.V.E.R.Y. GET request
:HTTP history: list of HTTP hosts, methods, url, etc

Repeater
--------

Allows you to modify HTTP methods' data for 'proof of concept' in hacking $TM.

	- best handles experimentation or **one-off testing**.

Target
------
:Summary: Whitelist|Blacklist websites for scope control

Defines the scope of your proxy.

	- including the $TM's site map.
