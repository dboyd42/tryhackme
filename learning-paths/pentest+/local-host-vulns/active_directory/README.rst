Active Directory
################
:Author: David Boyd
:Date: 2020-10-22

[Task 1] Introduction
*********************

Actvice Directory
=================

Active Directory
	is the **directory service** for Windows Domain Networks.
	[+] is a collection of machines and servers connected inside of domains,
	that are a collective part of a bigger forest of domains, that make up the
	Active Directory network. Active Directory contains many functioning bits
	and pieces (see: AD Components).

AD Components (Sections)
------------------------

	- Domain Controllers
	- Forests, Trees, Domains
	- Users + Groups
	- Trusts
	- Policies
	- Domain Services

Purpose
-------

The majority of large companies use Active Directory because it allows
for the control and monitoring of their user's computers through a single
domain controller.  It allows a single user to sign into ANY computer on the
active directory network and have access to his or her stored files and folders
in the server, as well as the local storage on that machine.  This allows for
any user in the company to use any machine that the company owns, without
having to set up multiple users on a machine.  Active Directory does it all for
you!

[Task 2] Physcial Active Directory
**********************************

The physical Active Directory is the servers and machines on-premise, these can
be anything from domain controllers and storage servers to domain user
machines; everything needed for an Acittve Directory environment besides the
software.

Domain Controllers
==================

Domain Controllers
	is a Windows server
	that has Active Directory Domain Services (AD DS) installed
	and has been promoted to a domain controller in the **forest**.
	[+] Domain controllers are **the center of Active Directory**
	[+] They control the rest of the domain.

	- holds the AD DS **data store**
	- handles authentication and authorization services
	- replicates updates from other domain controllers in the forest
	- allows admin access to manage domain resources

AD DS Data Store
================

AD DS Data Store
	holds the databases and processes
	needed to store and manage
	directory information, such as:
		- users
		- groups
		- services

AD DS Data Store outline:

	- contains the NTDS.dit
		- a db
		  that contains *all of the information of an AD DC*,
		  as well as,
		  *password hashes* for domain users.
		- stored by default in %SystemRoot%\NTDS
		- accessible only by the domain controller

Walkthrough
===========

+---+---------------------------------------+-------------------+
| # | Question                              | Answer            |
+===+=======================================+===================+
| 1 | What database does the AD DS contain? | NTDS.dit          |
+---+---------------------------------------+-------------------+
| 2 | Where is the NTDS.dit stored?         | %SystemRoot%\NTDS |
+---+---------------------------------------+-------------------+
| 3 | What type of machine can be a DC?     | Windows server    |
+---+---------------------------------------+-------------------+

Directory Service
=================
:alias: #name service, #name server
:see: #active directory, #AD DS

Directory Service
	maps the names of network resources to their respective network addresses.
	[+] It is a **shared information infrastructure** for locating, managing,
	administering and organizing everyday items and network resources, whcih
	can include volumes, folders, files, printers, users, groups, devices,
	phone numbers, and other objects.

Directory Server/Name Server
	provides the dirctory service.

Directory Service Terms
-----------------------
:object: a specific resource on the network.
:attribute(s): (a collection of) information about that particular object.

Domain
======

Domain
	[GENERIC] the **territory** governed by a single ruler or government; realm.
	[MATH] the set of values assigned to the independent variables of a
	function.
	[COMPUTERS] (A) A group of computers and devices on a network that are
	administered under the same protocol. (B) The top level in a **domain
	name**, indicating the type of organization, geographical location, or
	both, and officially designated in the suffix, as .edu for institutions of
	higher education.

Domain Name
	[COMPUTERS] name owned by a person or organization and consisting of an
	alphabetical or alphanumeric sequence followed by a suffic indicating the
	top-level domain: used as an internet address to identify the lcoation of
	particular web pages.

[Task 3] The Forest
*******************

foreset
	is what defines everything;
	it is the container
		that holds all of the other bits and pieces of the network together
		-- without the forest all of the other trees and domains
		   would not be able to interact.

The one thing to note when thinking of the forest is to not think of it too
literally -- it is a physical thing just as much as it is a figurative thing.

When we say "forest",
	it is only a way of describing the **connection**
	created between these trees and domains
	by the network.

Forest Overview
===============

A forest
	is a collection of one or more domain trees
	inside of an Active Directory network.
	It is what
	categorizes the parts of the network as a whole.

The Forest consists of these parts:

Trees
	A hierarchy of domains in Active Directory Domain Services

Domains
	Used to group and manage objects

Organizational Units (OUs)
	Containers for:
		- groups
		- computers,
		- users
		- printers
		- and other OUs

Trusts
	Allows users to access resources in other domains

Objects
	users, groups, printers, computers, shares

Domain Services
	- DNS Server
	- LLMNR
	- IPv6

Domain Schema
	Rules for object creation

