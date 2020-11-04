Wifi-Hacking-101
################
:Author: David Boyd
:Date: 2020-10-29

[Task 1] The Basics - An Intro to WPA
*************************************

Key Terms
=========
:SSID: The network "name" that you see when you try and connect
:ESSID: An SSID that may apply to multiple access points, eg a company
		office, normally forming a bigger network. For Aircrack they normally
		refer to the network you're attacking.
:BSSID: An access point MAC (hardware) address
:WPA2-PSK: Wifi networks that you connect to by providing a
		password that's the same for everyone
:WPA2-EAP: Wifi networks that you authenticate to by
		providing a username and password, which is sent to a RADIUS server.
:RADIUS: A server for authenticating clients, not just for wifi.

Quiz
====

#1 What type of attack on the encryption can you perform on WPA(2) personal?
:ANS: brute force (dictionary)

#2 Can this method be used to attack WPA2-EAP handshakes? (Yea/Nay)
:ANS: Nay (yes, but requires username)

#3 What three letter abbreviation is the technical term for the "wifi passwd?"
:ANS: PSK

#4 What's the minimum length of a WPA2 Personal password?
:ANS: 8

[Task 2] You're Being Watched - Capturing Packets to Attack
***********************************************************

The aircrack-ng suite consists of
==================================

	- aircrack-ng	(for "cracking" passwords)
	- airdecap-ng
	- airmon-ng		(for "monitoring" modes)
	- aireplay-ng
	- airodump-ng	(for "capturing" traffic)
	- airtun-ng
	- packetforge-ng
	- airbase-ng
	- airdecloak-ng
	- airolib-ng
	- airserv-ng
	- buddy-ng
	- ivstools
	- easside-ng
	- tkiptun-ng
	- wesside-ng

Quiz
====

#1 How do you put the interface “wlan0” into monitor mode with Aircrack tools?

airmon-ng start wlan0

#2 What is the new interface name likely to be after you enable monitor mode?
:ANS: wlan0mon

#3 What do you do if other processes are currently trying to use that network
adapter?

airmon-ng check kill

#4 What tool from the aircrack-ng suite is used to create a capture?

airodump-ng

#5 What flag do you use to set the BSSID to monitor?

--bssid

#6 And to set the channel?

--channel

#7 And how do you tell it to capture packets to a file?)

-w

[Task3] Aircrack-ng Let's Get Cracking
**************************************

In order to crack the password, we can either use aircrack itself or create a
hashcat file in order to use GPU acceleration. There are two different versions
of hashcat output file, most likely you want 3.6+ as that will work with recent
versions of hashcat.

Useful Information
==================
:BSSID: 02:1A:11:FF:D9:BD
:ESSID: 'James Honor 8'

#1 What flag do we use to specify a BSSID to attack?

-b

#2 What flag do we use to specify a wordlist?

-w

#3 How do we create a HCCAPX in order to use hashcat to crack the password?

-j

#4 Using the rockyou wordlist, crack the password in the attached capture.
What's the password?
:ANS: greeneggsandham

Walkthrough
===========

	aircrack-ng -b 02:1A:11:FF:D9:BD -w /usr/share/wordlists/rockyou.txt \
	NinjaJc01-01.cap



#5 Where is password cracking likely to be fastest, CPU or GPU?

GPU

