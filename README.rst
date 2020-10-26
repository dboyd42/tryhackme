README
#######
:Author: David Boyd
:Date: 2020-10-25

###
WSL
###

===================================
MSF > exploit completed no session
===================================

In some cases, you can get by with just using Windows > OpenVPN GUI for
connecting to TMs.  However, in using MSF and exploiting, it seems that I must
use:

.. code-block:: bash

	sudo openvpn bhat.ovpn

before hacking/reverse shelling.  Meaning, without WSL's OpenVPN, I can still
ping and "connect" to the TM, but without an Explicit use of ovpn in WSL,
there's no reverse shells.

