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

This room will require `OWASP Juice Shop (GitHub)
<https://github.com/bkimminich/juice-shop#from-sources>`_ or `OWASP Juice Shop
(TryHackMe) <https://tryhackme.com/room/owaspjuiceshop>`_

1. Read the overview and continue on into installation!
=======================================================
:Answer: [No answer needed]

[Task 2] Installation
*********************
:Requirements: Burpsuite

1. If you'll be installing Burp (as it's commonly referred to) from scratch, you'll need to first visit this link: `BurpSuite <https://portswigger.net/burp/communitydownload>`_
==================================================================================================================================================================
:Answer: [No answer needed]

2. Once you've reached the Port Swigger downloads page, go ahead and download the appropriate version for your operating system
===============================================================================================================================
:Answer: [No answer needed]

3. Burp Suite requires Java JRE in order to run. Download and install Java here: `Java <https://www.java.com/en/download/>`_
==================================================================================================================
:Answer: [No answer needed]

[Task 3] Gettin' [CA] Certified!
********************************
:Requirements: `Foxy Proxy <https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/`_

1. Launch Burp!
===============
:Answer: [No answer needed]

2. Once this pops-up, click 'Temporary project' and then 'Next'.
================================================================
:Answer: [No answer needed]

3. Next, we'll be prompted to ask for what configuration we'd like to use. For now, select 'Use Burp defaults'.
===============================================================================================================
:Answer: [No answer needed]

4. Finally, let's go ahead and Start Burp! Click 'Start Burp' now!
==================================================================
:Answer: [No answer needed]

5. Since we now have Burp Suite running, the proxy service will have started by default with it. In order to fully leverage this proxy, we'll have to install the CA certificate included with Burp Suite (otherwise we won't be able to load anything with SSL). To do this, let's launch Firefox now!)
========================================================================================================================================================================================================================================================================================================
:Answer: [No answer needed]

Note: you can use any browser as long as you set up a forward proxy for it.

6. Navigate to the following link to install FoxyProxy Standard. Go ahead and install this now!
===============================================================================================
:Answer: [No answer needed]

7. Next, we'll move onto adding the certificate for Burp!
=========================================================
:Answer: [No answer needed]

Setup Web Browser Proxy to proxy Burpsuite
------------------------------------------

**Foxy Proxy > Options > Add**

+------------------+-----------+
| Setting          | Value     |
+==================+===========+
| Title            | Burp      |
+------------------+-----------+
| Proxy Type       | HTTP      |
+------------------+-----------+
| Proxy IP address | 127.0.0.1 |
+------------------+-----------+
| Port             | 8080      |
+------------------+-----------+

**Save**

Web Browser > Proxy Extension > burp (enable)
---------------------------------------------

Click on the FoxyProxy extension icon again and select 'Burp'

8. With Firefox, navigate to the following address: http://localhost:8080
=========================================================================
:Answer: [No answer needed]

9. Click on 'CA Certificate' in the top right to download and save the CA Certificate
=====================================================================================
:Answer: [No answer needed]

10. Click on 'View Certificates'
================================
:Answer: [No answer needed]

11. Next, in the Authorities tab click on 'Import'
==================================================
:Answer: [No answer needed]

12. Navigate to where you saved the CA Certificate we downloaded previously. Click 'OK' once you've selected this certificate.
==============================================================================================================================
:Answer: [No answer needed]

13. Select 'OK' once you've done this. Congrats, we've now installed the Burp Suite CA Certificate!
===================================================================================================
:Answer: [No answer needed]

Overview
--------

Installing Burpsuite CA Certificate on Web Browser (Firefox)

	- Web Browser > http://localhost:8080 (127.0.0.1:8080)
	- Download CA Certificate
	- Menu > Preferences > Find in Preferences: cert
	- View Certificates > Import > cacert.der
	- [Checkbox] Trust the CA ti identify web sites
	- [Checkbox] Trust the CA ti identify email users

[Task 4] Burpsuite Features
***************************

payload
	items form our word list

set of payloads
	one wordlist

Overview of each BurpSuite section:
===================================

- **Proxy** - What allows us to funnel traffic through Burp Suite for further analysis
- **Target** - How we set the scope of our project. We can also use this to effectively create a site map of the application we are testing.
- **Intruder** - Incredibly powerful tool for everything from field fuzzing to credential stuffing and more
- **Repeater** - Allows us to 'repeat' requests that have previously been made with or without modification. Often used in a precursor step to fuzzing with the aforementioned Intruder
- **Sequencer** - Analyzes the 'randomness' present in parts of the web app which are intended to be unpredictable. This is commonly used for testing session cookies
- **Decoder** - As the name suggests, Decoder is a tool that allows us to perform various transforms on pieces of data. These transforms vary from decoding/encoding to various bases or URL encoding.
- **Comparer** - Comparer as you might have guessed is a tool we can use to compare different responses or other pieces of data such as site maps or proxy histories (awesome for access control issue testing). This is very similar to the Linux tool diff.
- **Extender** - Similar to adding mods to a game like Minecraft, Extender allows us to add components such as tool integrations, additional scan definitions, and more!
- **Scanner** - Automated web vulnerability scanner that can highlight areas of the application for further manual investigation or possible exploitation with another section of Burp. This feature, while not in the community edition of Burp Suite, is still a key facet of performing a web application test.)

1. Which tool in Burp Suite can we use to perform a 'diff' on responses and other pieces of data?
=================================================================================================
:Answer: Comparer

2. What tool could we use to analyze randomness in different pieces of data such as password reset tokens?
==========================================================================================================
:Answer: Sequencer

3. Which tool can we use to set the scope of our project?
=========================================================
:Answer: Target

4. While only available in the premium versions of Burp Suite, which tool can we use to automatically identify different vulnerabilities in the application we are examining?
=============================================================================================================================================================================
:Answer: Scanner

5. Encoding or decoding data can be particularly useful when examining URL parameters or protections on a form, which tool allows us to do just that?
=====================================================================================================================================================
:Answer: Decorder

6. Which tool allows us to redirect our web traffic into Burp for further examination?
======================================================================================
:Answer: Proxy

7. Simple in concept but powerful in execution, which tool allows us to reissue requests?
=========================================================================================
:Answer: Repeater

8. With four modes, which tool in Burp can we use for a variety of purposes such as field fuzzing?
==================================================================================================
:Answer: Intruder

9. Last but certainly not least, which tool allows us to modify Burp Suite via the addition of extensions?
==========================================================================================================
:Answer: Extender

[Task 5] Engage in Dark Mode
****************************

1. With Burp Suite launched, let's first navigate to the 'User options' tab.
============================================================================
:Answer: [No answer needed]

2. Now, click on the 'Look and feel' drop-down menu. Select 'Darcula'.
=======================================================================
:Answer: [No answer needed]

3. Finally, close and relaunch Burp Suite to have dark theme (or whichever theme you picked) take effect.
=========================================================================================================
:Answer: [No answer needed]

[Task 6] Proxy
**************

Deploy the VM attached to this task!

1. To complete this task you need to connect to the TryHackMe network through OpenVPN. If you're using the in-browser machine this isn't needed (but make sure you're accessing the machine and using Burp inside the in-browser machine).
==========================================================================================================================================================================================================================================
:Answer: [No answer needed]

2. By default, the Burp Suite proxy listens on only one interface. What is it? Use the format of IP:PORT
========================================================================================================
:Answer: [No answer needed]

3. In Burp Suite, navigate to the Intercept sub-tab of the Proxy section. Enable Intercept
==========================================================================================
:Answer: [No answer needed]

4. Take a look at the actions, which shortcut allows us to forward the request to Repeater?
===========================================================================================
:Answer: CTRL-R

5. How about if we wanted to forward our request to Intruder?
=============================================================
:Answer: CTRL-I

6. What is the name of the first section wherein general web requests (GET/POST) are saved?
===========================================================================================
:Answer: HTTP history

7. Defined in RFC 6455 as a low-latency communication protocol that doesn't require HTTP encapsulation, what is the name of the second section of our saved history in Burp Suite? These are commonly used in collaborate application which require real-time updates (Google Docs is an excellent example here).
=================================================================================================================================================================================================================================================================================================================
:Answer: WebSockets history

8. Before we move onto exploring our target definition, let's take a look at some of the advanced customization we can utilize in the Burp proxy. Move over to the Options section of the Proxy tab and scroll down to Intercept Client Requests. Here we can apply further fine-grained rules to define which requests we would like to intercept. Perhaps the most useful out of the default rules is our only AND rule. What is it's match type?
===================================================================================================================================================================================================================================================================================================================================================================================================================================================
:Answer: URL

9. How about it's 'Relationship'? In this situation, enabling this match rule can be incredibly useful following target definition as we can effectively leave intercept on permanently (unless we need to navigate without intercept) as it won't disturb sites which are outside of our scope - something which is particularly nice if we need to Google something in the same browser.
==========================================================================================================================================================================================================================================================================================================================================================================================
:Answer: Is in target scope

[Task 7] Target Definition
**************************

1. Before leaving the Proxy tab, switch Intercept to disabled. We'll still see the pages we navigate to in our history and the target tab, just having Intercept constantly stopping our requests for this next bit will get old fast.
======================================================================================================================================================================================================================================
:Answer: [No answer needed]

2. Navigate to the Target tab in Burp. In our last task, Proxy, we browsed to the website on our target machine (in this case OWASP Juice Shop). Find our target site in this list and right-click on it. Select 'Add to scope'.
=================================================================================================================================================================================================================================
:Answer: [No answer needed]

3. Clicking 'Add to scope' will trigger a pop-up. This will stop Burp from sending out-of-scope items to our site map.
========================================================================================================================================================
:Answer: [No answer needed]

4. Select 'Yes' to close the popup.
===================================
:Answer: [No answer needed]

5. Browse around the rest of the application to build out our page structure in the target tab. Once you've visited most of the pages of the site return to Burp Suite and expand the various levels of the application directory. What do we call this representation of the collective web application?
=========================================================================================================================================================================================================================================================================================================
:Answer: site map

6. What is the term for browsing the application as a normal user prior to examining it further?
================================================================================================
:Answer: happy path

7. One last thing before moving on. Within the target tab, you may have noticed a sub-tab for issue definitions. Click into that now.
=====================================================================================================================================
:Answer: [No answer needed]

8. The issue definitions found here are how Burp Suite defines issues within reporting. While getting started, these issue definitions can be particularly helpful for understanding and categorizing various findings we might have.  Which poisoning issue arises when an application behind a cache process input that is not included in the cache key?
===========================================================================================================================================================================================================================================================================================================================================================
:Answer: Web cache poisoning

[Task 8] Puttin' it on Repeat[er]
*********************************

[Task 9] Help! There's an Intruder!
***********************************

[Task 10] As it turns out the machines are better at math than us
*****************************************************************

[Task 11] Decoder and Comparer
******************************

[Task 12] Installing some Mods [Extender]
*****************************************

[Task 13] But wait, there's more!
*********************************

[Task 14] Extra Credit
**********************

.. Additional Information
.. **********************
..
.. Intruder
.. --------
..
.. Allows repeat testing nce a 'proof of conecpt' has been established.
..
.. **Common Usage:**
..
.. 	- enumerating:
.. 		- identifers (usernames, etc)
.. 		- cycling thorugh predicatble session/password recovery tokens
.. 		- attempting simple password guessing
.. 	- harvesting (through grepping our responses)
.. 		- data from profiles
.. 		- other pages of interest
.. 	- fuzzing for vulnerabilities
.. 		- SQL injection
.. 		- XSS
.. 		- file path traversal
..
.. **Attack Type:**
..
.. positions = fields (username, password, whatever, etc.)
.. payload = item in wordlist
.. set of payloads = one wordlist
..
.. Sniper
.. 	The most popular attack type,
.. 	this cycles through out selected positions, putting the next available
.. 	payload (items from our wordlist) in each position in turn.
.. 	This uses only one set of payloads (one wordlist)
..
..
.. Battering ram
.. 	Similar to Sniper,
.. 	Battering Ram uses only one set of payloads.  Unlike Sniper,
.. 	Battering ram puts every payload into *every selected position*.
.. 	Think about how a bettering ram makes contact across a large surface with a
.. 	single surface, hence the name Battering ram for this attack type.
..
.. Pitchfork
.. 	Allows us to use *multiple payload sets* (one per position selected)
.. 	and iterate through both paylod sets *simulataneously*.
.. 	For example, if we selected two positions
.. 		(say a username field and a password field),
.. 	we can provide a username and password payload list.
.. 	Intruder will then cycle through the combinations of usernames & passwords,
.. 	resulting in a total number of combinations equalling the
.. 	*smallest payload* set provided.
..
.. Cluster bomb
.. 	Allows us to use multiple payload sets (one per position selected) and
.. 	iterate through all combinations of the payload lists we provide.
.. 	For example, if we selected two poistions
.. 		(say a username field and a password field),
.. 	we can provide a username and password payload list.
.. 	Intruder will then cycle through the combinations of usernames & passwords,
.. 	resulting in a total number of combinations equalling
.. 	*usernames x passwords*.
.. 	:NOTE: Can get lengthy if you're using the community edition of Burp.
..
..
.. positions = fields (username, password, whatever, etc.)
.. payload = item in wordlist
.. set of payloads = one wordlist
..
.. +---------------+-----------------------------+-----------------------------------------------+
.. | Attack Type   | Payload (nSets/position)    | Iteration (set/position)                      |
.. +===============+=============================+===============================================+
.. | Sniper        | single (payload++/position) | iterate next payload in each position in turn |
.. +---------------+-----------------------------+-----------------------------------------------+
.. | Battering ram | single (one/position)       | iterate simulataneiously                      |
.. +---------------+-----------------------------+-----------------------------------------------+
.. | Pitchfork     | multi (multi/position)      | iterate simulataneiously                      |
.. +---------------+-----------------------------+-----------------------------------------------+
.. | Cluster bomb  | multi (one/position)        | iterate all possible combos                   |
.. +---------------+-----------------------------+-----------------------------------------------+
..
.. Poxy
.. ----
.. :Intercept: On|Off: Decide if proxy will intercept E.V.E.R.Y. GET request
.. :HTTP history: list of HTTP hosts, methods, url, etc
..
.. Repeater
.. --------
..
.. Allows you to modify HTTP methods' data for 'proof of concept' in hacking $TM.
..
.. 	- best handles experimentation or **one-off testing**.
..
.. Target
.. ------
.. :Summary: Whitelist|Blacklist websites for scope control
..
.. Defines the scope of your proxy.
..
.. 	- including the $TM's site map.
