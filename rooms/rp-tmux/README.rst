README
#######
:Author: David Boyd
:Date: 2020-06-02

nmap
====

	- sV - probe open ports to determine services/Version info
	- vv - increase verbosity level
	- sC - Script sCan --equivalen to --script=Default

.tmux.config
============

.. code-block:: Tmux

	### Prevent renaming after setting a static name
	set -g allow-rename off

	### Search mode VIM (default is emac)
	set-window-option -g mode-keys vi

	### Plug-ins
	run-shell /opt/tmux-logging/logging.tmux    # log sessions
        	                                    # /root/tmux-history-<SESSION>.log
	### Display vi key bindings
	# list-keys -T vi-copy
