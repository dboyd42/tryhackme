Start Here
##########

OpenVPN
*******

Windows 10
==========

OpenVPN GUI > <usrname>.ovpn

WSL
===

1.	Can run through Windows 10 OpenVPN GUI
2.	If invoking listeners/reverse shells/etc on WSL;
	THEN disconnect Windows OpenVPN GUI and start `Linux`_ vpn.

Linux
=====

.. code-block:: Bash

	sudo openvpn <usrname>.ovpn

Troubleshooting
***************

WSL
===

MSF > exploit completed no session
----------------------------------

In some cases, you can get by with just using Windows > OpenVPN GUI for
connecting to TMs.  However, in using MSF and exploiting, it seems that I must
use

.. code-block:: bash

	sudo openvpn bhat.ovpn

before hacking/reverse shelling.  Meaning, without WSL's OpenVPN, I can still
ping and "connect" to the TM, but without an Explicit use of ovpn in WSL,
there's no reverse shells.

