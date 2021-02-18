HTTP Web Fundamentals
#####################
:Author: David Boyd
:Date: 2020-10-07
:Topics: requests and responses, web servers, cookies, CTF
:Task2: How do we load website?
:Task3: More HTTP - Verbs and request formats
:Task4: Cookies, tatsy!
:Task5: Mini CTF

Task2 How do we load website?
=============================

Finding the Server
------------------

1.	DNS request is made.

The IP address uniquely identifies each internet connected device, like a web
server or your computer.

Loading some content
--------------------

GET
	[+] an HTTP verb, which are different types of requests (covered later).

web server
	a SW that receives and responds the HTTP(S) requests.
	[+] Apache, Nginx, MS IIS

web page content
	a combination of HTML, CSS, and JavaScript.
	[+] HTML - structure of the page and content.
	[+] CSS - how the page looks (think design)
	[+] JavaScript - prgmming language that runs in the browser and allows you
					 to make the pages *interactive* or *load extra content*.

Once the browser knows the server's IP address, it can ask the server for the
web page.  This is doen with a **HTTP GET request**. The server will respond to
the GET request with the web page content.  If the web page is loading extra
resources, like JavaScript, images, or CSS files, those will be retrieved in
separate GET requests.

.. code-block:: Wireshark

	# Showing HTTP requests that laod a website
	3.37731	100.70.172.11	143.204.178.68	HTTP 591 GET /online HTTP/1.1			// Request
	3.38416	143.204.178.68	100.70.172.11	HTTP  60 HTTP/1.1 200 OK (text/html)	// Response
	3.46491	100.70.172.11	143.204.178.68	HTTP 504 GET /favicon.ico HTTP/1.1		// Request
	3.47654	143.204.178.68	100.70.172.11	HTTP 178 HTTP/1.1 200 OK (PNG)			// Response

Most websites today use HTTPS with TLSv1.3 for encryption

Many CTFs are based around websites;
	IF (-p80 is open) {
		web_server = exploitable/attackable;
	}

Task3 More HTTP - Verbs and request formats
===========================================

HTTP_methods = HTTP_verbs = 9

GET requests
	used to retrieve content

POST requests
	used to send data to a web server
	[+] adding a comment -or- performing a login

HTTP request
------------

GET Headers
	can tell from which SW the user requested from (Chorme Version 80, from Win10)
	[+] useful for forensics and analysing packet captures

**Example:**

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chome/80.0.3987.122 Safari/537.36

+-----------+---------------------------------+--------------------------------+
| Section # | Example                         | Description                    |
+===========+=================================+================================+
| 1         | GET /main.js HTTP/1.1           | verb+path for the server       |
+-----------+---------------------------------+--------------------------------+
| 2         | Host: 192.168.170.129:8081      | headers - give more info about |
|           | Connection: keep-alive          | your request. [+] cookies are  |
|           | User-Agent: Mozilla/5.0...      | sent in this.request.header    |
|           | Accept: */*                     |                                |
|           | Referer: http://192....:8081    |                                |
|           | Accept-Encoding: gzip, deflate  |                                |
|           | Accept-Language: en-GB,en-US... |                                |
+-----------+---------------------------------+--------------------------------+
| 3         |                                 | Body of Request -              |
|           |                                 | [+] POST requests - content is |
|           |                                 | sent to the server.            |
|           |                                 | [+] GET requests - body mostly |
|           |                                 | ignored by server; but is      |
|           |                                 | allowed.                       |
+-----------+---------------------------------+--------------------------------+

Responses
---------
:URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

Response Headers
	offer info about
		[+] the web server
		[+] cookies (useful later on)

The server replies with a *reponse*.  Response follows a similar structure to
the request, but the first line describes the *status* rather than a verb and a
path. Ie) 404

**Status Codes**

+---------+-----------------------------------------------------------+
| Range   | Description                                               |
+=========+===========================================================+
| 100-199 | Information                                               |
+---------+-----------------------------------------------------------+
| 200-299 | Success (200 OK is the "normal" response for a GET)       |
+---------+-----------------------------------------------------------+
| 300-399 | Redirects (the information you want IS ELSEWHERE)         |
+---------+-----------------------------------------------------------+
| 400-499 | Client errors (You fucked up; Ie: asking 4smthg != exist) |
+---------+-----------------------------------------------------------+
| 500-599 | Sever errors (Svr fucked up; it's their fault)            |
+---------+-----------------------------------------------------------+

**Response Structure**

Response header      - status of the request
Response body (GET)  - web content or info(JSON)
Response body (POST) - status message/similar

**GET Response Example**

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 28
Content-Type: application/javascript; charset=utf-8
Last-Modified: Wed, 12 Feb 2020 12:51:33 GMT
Date: Thu, 27 Feb 2020 21:7:30 GMT

console.log("Hello, World!")

Questions
---------

What verb would be used for a login? POST

What verb would be used to see your bank balance once you're logged in? GET

Does the body of the GET request matter? No.

What's the status code for "I'm a teapot"? 418

What status code will you get if you're unauthorized? 401

Task4 Cookies, tatsy!
=====================

What are cookies?
-----------------

Cookies are small bits of data that are stored in your browser. Each browser
will store them separately, so cookies in Chrome won't be available in
Firefox. They have a huge number of uses, but the most common are either
session management or advertising (tracking cookies). Cookies are normally
sent with every HTTP request made to a server.

Why Cookies?
------------

Because HTTP is stateless (Each request is independent and no state is
tracked internally), cookies are used to keep track of this. They allow sites
to keep track of data like what items you have in your shopping cart, who you
are, what you've done on the website and more.

Cookies can be broken down into several parts. Cookies have a name, a value,
an expiry date and a path. The name identifies the cookie, the value is where
data is stored, the expiry date is when the browser will get rid of the
cookie automatically and the path determines what requests the cookie will be
sent with. Cookies are normally only sent with requests to the site that set
them (Weird things happen with advertising/tracking).

The server is normally what sets cookies, and these come in the response
headers (Set-Cookie). Alternatively, these can be set from JavaScript inside
your browser.

Using cookies
-------------

When you log in to a web application, normally you are given a Session Token.
This allows the web server to identify your requests from someone else's.
Stealing someone else's session token can often allow you to impersonate them.

Manipulating cookies
--------------------

Using your browser's developer tools, you can view and modify cookies. In
Firefox, you can open the dev tools with F12. In the Storage tab, you can see
cookies that the website has set. There's also a + button to allow you to
create your own cookies which will come in handy in a minute. You can modify
all cookies that you can see in this panel, as well as adding more.

Alternatives - useful to know
-----------------------------

Slowly, for some uses, LocalStorage and SessionStorage are used instead. This
has a similar functionality but isn't sent with HTTP requests by default.
These are HTML5 features.

More on cookies
---------------
:URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

Task5 Mini CTF
==============

.. code-block:: Bash

	# What's the GET flag?
	curl 10.10.147.16:8081/ctf/get

	# What's the POST flag?
	curl -X POST --data flag_please 10.10.147.16:8081/ctf/post

	# What's the "Get a cookie" flag?
	curl -c getacookie.txt 10.10.147.16:8081/ctf/getcookie; cat getacookie.txt

	# What's the "Set a cookie" flag?
	curl -b flagpls=flagpls 10.10.147.16:8081/ctf/sendcookie

