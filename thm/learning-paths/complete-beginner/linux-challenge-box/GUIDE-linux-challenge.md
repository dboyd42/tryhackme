# Linux Challenges Walkthrough

Date          | 2020-05-31          |
--------------|---------------------|
Learning Path | Complete Beginner   |
Box           | Linux Challenge     |

## 1) Introduction (init access)

Username: garry

Password: letmein

Q# | Question | How-to | Answer |
---|----------|--------|--------|
1  | How many visible files can you see in garrys home directory? | ls | 3 |

## 2) The Basics

Q# | Question | How-to | Answer |
---|----------|--------|--------|
1  | What is flag 1? | cat flag1.txt | f40dc0cff080ad38a6ba9a1c2c038b2c |
2  | What is flag 2? | su bob; linuxrules; cat ~/flag2.txt | 8e255dfa51c9cce67420d2386cede596 |
3  | Flag 3 is located where bob's bash history gets stored. | cat ~/.bash_history | 9daf3281745c2d75fc6e992ccfdedfcd |
4  | Flag 4 is located where cron jobs are created | crontab -e(ditor) | dcd5d1dcfac0578c99b7e7a6437827f3 |
5  | Find and retrieve flag 5 | find / -name flag5\* 2>/dev/null | cat /lib/terminfo/E/flag5.txt | bd8f33216075e5ba07c9ed41261d1703 |
6  | "Grep" through flag 6. 1st 2 chars=c6 | find / -name flag6.txt 2>/dev/null; cat /home/flag6.txt \| grep \\bc9 | c9e142a1e25b24a837b98db589b08be5 |
7  | Look at system process for flag7 | ps -aux \| grep flag | 274adb75b337307bd57807c005ee6358 | 274adb75b337307bd57807c005ee6358 |
8  | De-compress flag8 | tar -xvf flat8.tar.gz && cat flag8.txt | 75f5edb76fe98dd5fc9f577a3f5de9bc |
9  | Hosts file for flag9 | cat /etc/hosts | dcf50ad844f9fe06339041ccc0d6e280 |
10 | Find other users on system for flag10 | cat /etc/passwd | 5e23deecfe3a7292970ee48ff1b6d00c |

##### Notes

**cron** is the name of tool, **crontab** is the *file* that lists the jobs that **cron** executes --and those jobs are called, **cronjobs**.  // Note: file locations vary by OS.

**/etc directory** contains *system-wide configuration files* that are editable administrator.  // Note: *user-specific config files* are located in each user's **/home directory**.

the **hosts** file is an OS file that **maps hostnames to IP addresses** in plain text (.txt).

tool                     | description   |
-------------------------|---------------|
grep **\\\\b**           | stands for *boundary* ~= beginning of a word.  Can use either double backslash or '\b'. |
tar -x, --extract, --get | extract files from an archive        |
tar -v, --verbose        | verbosely list files processed       |
tar -f, --file ARCHIVE   | use archive file or device ARCHIVE   |
ps -a                    | show 'a'll processes for 'a'll users |
ps -u                    | show 'u'ser/owner of the processes   |
ps -x                    | show unattached terminal processes   |


## 3) Linux Functionality

### Init access (given)

Username: alice

Password: TryHackMe123

#### Q1) Run the command flag11.  Locate where your command alias are stored and get flag 11.

```bash
cd /home/
for dir in */; do
    cd $dir
    cat .bashrc | grep -i flag;
    cat .bash_aliases | grep -i flag;
    cd ../;
done
```

Flag11: b4ba05d85801f62c4c0d05d3a76432e0

#### Q2) Flag12 is located where MOTD's are usually found on Ubuntu.

**MOTD (Message of the Day)**

```bash
cat /etc/update-motd.d/* | grep -i flag
```

Flag12: 01687f0c5e63382f1c9cc783ad44ff7f

#### Q3) Find diff b/t 2 script files to find flag 13

```bash
find / -iname *flag13*
cd /home/bob/flag13/
vimdiff script1 script2
```

Flag13: 3383f3771ba86b1ed9ab7fbf8abab531

#### Q4) Where on the file system are logs typically stored?

```bash
cd /var/log/
cat flagtourteen.txt
```

**/var directory** stands for *variable* (it holds variable data, the directory it contains are changing in size every time).  I.e.) logs!

Flag14: 71c3a8ad9752666275dadf62a93ef393

#### Q5) Can you find information about the system, such as the kernal version, etc?

```bash
cat /etc/lsb-release
```

Flag15: a914945a4b2b5e934ae06ad6f9c6be45

#### Q6) Flag16 lies within in another system mount

```bash
cd /media/f/l/a/g/1/6/is/cab4b7cae33c87794d82efa1e7f834e6/
```

Note: just hit tab after /media/ a bunch of times, lol.

Flag16: cab4b7cae33c87794d82efa1e7f834e6

#### Q7) Login to alice's account using her private key and get flag 17.

```bash
cat /home/alice/flag17
```

Note: did not have to login using private key... ?!

Flag17: 89d7bce9d0bab49e11e194b54a601362

#### Q8) Find the hidden flag 18

```bash
cat /home/alice/.flag18
```

Flag18: c6522bb26600d30254549b6574d2cef2

#### Q9) Read the 2345th line of the file that contains flag19.
```bash
head -n 2345 flag19 | tail -n 1
```

Flag19: 490e69bd1bf3fc736cce9ff300653a3b

## 4) Data Representation, Strings, and Premissions

#### Q1)  Flag 20

```bash
base64 --decode flag20
```

**base64** is a binary-to-text encoding scheme that formats 8-bits into 6 bits (2^6=64!)
It works by taking three ASCII letters' bits and dividing them into four sections (6 bits each).
Each new 6-bit 'word' is mapped to a base64 scheme (table).
**Because of its limited scheme, its easily recognizable and often ends with one or more '=' due to extra chars needed for division.

Flag20: 02b9aab8a29970db08ec77ae425f6e68

#### Q2) Inspect the flag21.php file.  Find the flag.

```bash
find / -iname flag21.php 2>/dev/null
cat /home/bob/flag21.php
file /home/bob/flag21.php               # CRLF terminators = Windows file
cat /home/bob/flag21.php | less         # or open through vim
````

Flag21: g00djob

##### Notes

**CRLF** = "Carriage Return, Line Feed" - it's a DOS hangover from the olden
days from when some devices required a Carriage Return, and some devices
required a Line Feed to get a new line, so MS decided to just make a new-line
have both characters, so that they would output correctly on all devices.
*Linux/UNIX only uses LF terminators.*

CRLF outcomes: CRLF injection, dox2unix/unix2dox conversion

**PHP** is a server side scripting language that is used to develop websites
or web applications.  *PHP stands for Hypertext Pre-processor, that earlier
stood for Personal Home Pages.*  PHP scripts can only be interpreted on a
server that has PHP installed.

PHP '$ _ POST' is a PHP super global variable which is used to collect form
data after submitting an HTML form with method="post".  $ _ POST is also widely
used to pass variables.

#### Q3) Locate and read flag 22.  Its represented as hex.

```bash
find / -iname flag22* 2>/dev/null
xxd -r p /home/alice/flag22
```

Note: xxd -r(evert) -p(lain); where -p(lain) prints output plain hexdump style.

Flag22: 9d1ae8d569c83e03d8a8f61568a0fa7d

#### Q4) Locate, read and reverse flag 23.

```bash
rev flag23
```

rev - reverse lines characterwise.

Flag23: ea52970566f4c090a7348b033852bff5

#### Q5) Analyse the flag 24 compiled C program. Find a command that might reveal human readable strings when looking in the source code.

```bash
strings flag24
````

Flag24: hidd3nStr1ng

#### Q6) Flag 25 does not exists.

SKIP.

#### Q7) Find flag 26 by searching the all files for a string that begins with 4bceb and is 32 characters long.

```bash
# find's '-exec' MUST include a ';'
find / -xdev 2>/dev/null -exec grep '^4bceb' {} \;
# OR include 32 total chars
find / -xdev 2>/dev/null -exec grep '$4bceb.\{28\}' {} \;
```

Flag26: 4bceb76f490b24ed577d704c24d6955d

#### Q8) Flag27, owned by root.

Tried: sudo -l to find sudoers (alice comes close, but can't do anything :( )
Tried: alice $ chown/chmod /home/flag27


#### Q9) Whats the linux kernal version?

```bash
uname -a
```

Answer: 4.4.0-1075-aws

#### Q10) Find the file called flag 29 and do the following operations on it:

    1. remove all the spaces in the file
    2. remove all new line spaces.
    3. split by comma and get the last element in the split

Answer:


## 5) SQL, FTP, Groups, and RDP




