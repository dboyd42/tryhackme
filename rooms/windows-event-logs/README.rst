Windows Event Logs
##################
:Author: David Boyd
:Date: 2021-02-17

[Task 1] What are event logs?
*****************************
:Note: Win10 > Store > Remote Desktop > $TM:administer:blueT3aming!

Intro
=====

Event logs
	record events taking place in the execution of a system to provide an audit
	trail that can be used to understand the activity of the system and to
	diagnose problems.  They are essential to understand the activities of
	complex systems, particularly in applications with little user interaction
	(such as server applications).

	[+] Event logs can also be useful to combine log file entries from
	multiple sources.  This approach, in combination with statistical analysis,
	may yield correlations between seemingly unrelated events on different
	servers.

SIEMs (Security Information and Event Management): Splunk, Elastic
	allows you to query the logs from multiple devices instead of manually
	connecting to a single device to view its logs.

Syslog
	Linux and macOS name/version for their logging system.

Questions
=========

Let's begin...
--------------
:Answer: [No answer needed]

[Task 2] Event Viewer
*********************

Glossary
========

MMC
	Microsoft Management Console

Intro
=====

The Windows Event Logs are not text files that can be viewed using a text
editor.  However, the raw data can be translated into XML using the Windows
API.  The events stored in these log files are stored in a proprietary binary
format with a **.evt** or **.evtx** extension.  The log files with the **.evtx**
file extension typically reside in `C:\Windows\System32\winevt\Logs`.

3 ways of accessing event logs w/in Windows
-------------------------------------------

	1. **Event Viewer** (GUI-based application)
		- CMD/PS: `eventvwr.msc`

	2. **Wevtutil.exe** (CLI tool)
	3. **Get-WinEvent** (PS cmdlet)

Event Viewer's 3 Main Panes
---------------------------

	1. [Left] a hierarchical tree listing of the event log providers
	2. [Middle] general overview & summary *OR* events specific to a selected provider
	3. [Right] actions

Left Pane (Event Log Providers)
===============================

The 5 Types of Events
---------------------
:URL: https://docs.microsoft.com/en-us/windows/win32/eventlog/event-types

+-------------+---------------------------------------------------------------+
| Event type  | Description                                                   |
+=============+===============================================================+
| Error       | An event that indicates a significant problem such as a loss  |
|             | data or functionality.  For example, is a services fails to   |
|             | load during startup, an Error event is logged.                |
+-------------+---------------------------------------------------------------+
| Warning     | An event that is not necessarily significant, but may         |
|             | indicate a possible future problem.  For example, when disk   |
|             | space is low, a Warning event is logged.  If an application   |
|             | can recover from an event without loss of functionality or    |
|             | data, it can generally classify the event as a Warning event. |
+-------------+---------------------------------------------------------------+
| Information | An event that describes the successful operation of an        |
|             | application driver, or service.  For example, when a network  |
|             | driver loads successfully, it may be appropriate to log an    |
|             | Information event.  Note that it is generally inappropriate   |
|             | for a desktop application to log an event each time it starts |
+-------------+---------------------------------------------------------------+
| Success     | An event that records an audited security attempt that is     |
| Audit       | successful.  For example, a user's successful attempt to log  |
|             | on to the system is logged as a Success Audit event.          |
+-------------+---------------------------------------------------------------+
| Failure     | An event that records an audited security access attempt that |
| Audit       | fails.  For example, if a user tries to access a network      |
|             | drive and fails, the attempt is logged as a Failure Audit     |
|             | Event.                                                        |
+-------------+---------------------------------------------------------------+

The 4++ Types of Windows Logs
-----------------------------
:URL: https://docs.microsoft.com/en-us/windows/win32/eventlog/eventlog-key

+-------------+--------------------------------------------------------------+
| Log         | Description                                                  |
+=============+==============================================================+
| Application | Contains events logged by applications.  For example, a DB   |
|             | application might record a file error.  The application      |
|             | developer decides which event to record.                     |
+-------------+--------------------------------------------------------------+
| Security    | Contains events such as in/valid logon attempts, as well as  |
|             | events related to resource use such as creating, opening, or |
|             | deleting files or other objects.  An administrator can start |
|             | auditing to record events in the security log.               |
+-------------+--------------------------------------------------------------+
| System      | Contains events logged by system components, such as the     |
|             | failure of a driver or other system component to load during |
|             | startup.                                                     |
+-------------+--------------------------------------------------------------+
| *CustomLog* | Contains events logged by applications that create a custom  |
|             | log.  Using a custom log enables an application to control   |
|             | the size of the log or attach ACLs for security purposes     |
|             | without affecting other applications.                        |
+-------------+--------------------------------------------------------------+

Applications and Services Logs
------------------------------

PowerShell
^^^^^^^^^^
:Path: `Microsoft > Windows > PowerShell > Operational`

PowerShell will log operations from the engine, providers, and cmdlets to the
Windows event log.

To **Clear Log** and/or find **log location**:
`[Rt-click] Operational > Properties`

Middle Pane (General Overview & Summary | Event Specific)
=========================================================

Top Pane
--------

+---------------+------------------------------------------------------------+
| Column        | Description                                                |
+===============+============================================================+
| Level         | event type                                                 |
+---------------+------------------------------------------------------------+
| Date and Time | when the event was logged                                  |
+---------------+------------------------------------------------------------+
| Source        | name of the software that logged the event                 |
+---------------+------------------------------------------------------------+
| Event ID      | Events are identified by IDs (Event ID).  Note that Event  |
|               | IDs are not unique.  Meaning that Event ID 4103 is related |
|               | to Executing Pipeline, but will have an entirely different |
|               | meaning in another event log.                              |
+---------------+------------------------------------------------------------+
| Task Category | Event Category.  This entry will help you organize events  |
|               | so that Event Viewer can filter them.  The event 'Source'  |
|               | defines this column.                                       |
+---------------+------------------------------------------------------------+

Bottom Pane
-----------

2 tabs: **General** and **Details**.

	- **General** is the default view, and the rendered data is displayed.
	- **Details** has 2 options: *Friendly* view and *XML* view.

Right Pane (Actions)
====================

`Open Saved Log...`
	useful if the remote machine can't be accessed.  The logs can be provided
	to the analyst.

`Create Custom View` ~== `Filter Current Log`

`[Rt-click] Event Viewer (Local) > Connect to Another Computer...`
	view event logs from another computer.

Questions
=========

For the questions below, use Event Viewer to analyze **Microsoft-Windows-PowerShell/Operational** log.
------------------------------------------------------------------------------------------------------
:Answer: [No answer needed]

What is the Event ID for the first event?
-----------------------------------------
:Answer: 40961

Note: If you launched PS after deploying VM, the first Event ID would have
changed.  Recommend re-deploying machine for further questions.

What are the total number of events if you filter on Event ID 4104?
--------------------------------------------------------------------
:Answer: 181

Note: Without re-deploying machine, I filtered out 233 4104 Event IDs.  After
re-deploying, I was able to filter 133 Event IDs.  I iterated from 133 until
THM displayed 'Correct Answer'.  My original method was from `Actions > Filter
Current Log...` to s/<All Event IDs>/4104.  To verify I filtered the logs
correctly, the middle pane displays: *Filtered: Log:
Microsoft-Windows-PowerShell/Operation; Source; Event ID: 4104. Number of
events: 133*.  I'm unsure as to why I couldn't get the correct answer.

What is the Task Category for Event ID 4104?
--------------------------------------------
:Answer: Execute a Remote Command

For the questions below, use Event Viewer to analyze the Windows PowerShell log.
--------------------------------------------------------------------------------
:Answer: [No answer needed]

What are the total number of events?
------------------------------------
:Answer: 421

Note: Same issue with the filter question.  Without any filter, the middle top
pane reads: *Operational Number of events: 373*.  I'm unsure as to why I'm not
getting the correct answer.

[Task 3] wevtutil.exe
*********************

[Task 4] Get-WinEvent
*********************

[Task 5] XPath Queries
**********************

[Task 6] Event IDs
******************

[Task 7] Putting theory into practice
*************************************

[Task 8] Conclusion
*******************

