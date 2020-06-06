Start Here
##########

OpenVPN
=======

Windows 10
----------

OpenVPN > bhat1.ovpn

Additionally let through host firewall as new rule > program > inbound.
Don't know if that made a difference though...?

.. code-block :: Windows GUI
	Title: OpenVPN - Check Connection
	IP Address: 10.10.243.142
	Expires: 1hr--
	[Button] Add 1 hour
	[Button] Terminate

Completed

Linux
-----

.. code-block:: Bash

	sudo openvpn bhat.ovpn

