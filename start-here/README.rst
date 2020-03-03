README
#######
:Author: David Boyd
:Date: 2020-03-03
:site: https://www.hackthebox.eu
:site: https://codeburst.io/hack-the-box-how-to-get-invite-code-56e369fc8dae

Getting Started
===============

#1	Download your connection pack
#2	sudo openvpn bhat.ovpn
#3	find IP address of attackable machine on the 'Active Machines' page


Invite Code
===========

Broswer Developer Tools:

.. code-block :: Browser

	makeInviteCode()


	# enctype: "BASE64"
	SW4gb3JkZXIgdG8gZ2VuZXJhdGUgdGhlIGludml0ZSBjb2RlLCBtYWtlIGEgUE9TVCByZXF1ZXN0IHRvIC9hcGkvaW52aXRlL2dlbmVyYXRl

	# base64 --decode msg.txt
	In order to generate the invite code, make a POST request to /api/invite/generate

.. code-block :: Bash

	# Make a POST request
	curl -XPOST https://www.hackthebox.eu/api/invite/generate

	# return
	{"success":1,"data":{"code":"QU5XQVQtRU5YUkotWUZMV0ItTFNRTE0tTFhWUkc=","format":"encoded"},"0":200}

	# assume prev coding format if none given (base64)
	base64 --decode post.txt

	# return
	ANWAT-ENXRJ-YFLWB-LSQLM-LXVRG

