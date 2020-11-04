Vulnversity Walkthrought
########################
:Author: David Boyd
:Date: 2020-10-26

Learn to better understand systemd / systemctl services and their unit files.

PrivEsc
*******

systmd / systemctl
==================
:URL: https://www.howtogeek.com/687970/how-to-run-a-linux-program-at-startup-with-systemd/
:URL: https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6

PHP Reverse Shell
-----------------

.. code-block:: bash

	wget https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.ph://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php

[Task4] Compromise the Webserver
********************************

Issue: Couldn't get a fileextension to go through --even the correct answer.
============================================================================
:Platform: Burp Suite
:Status: Resolved (mostly)
:Reason: Percent-Encoding enabled
:Quickfix: Intruder > Payloads > Payload Encoding > [checkbox] disable
:Issue Location: Post attack > Request > Position Param = "a%2aphmtl" (!=want)

Reverse Shell
	focing RHOST to connect to LHOST (you!)

