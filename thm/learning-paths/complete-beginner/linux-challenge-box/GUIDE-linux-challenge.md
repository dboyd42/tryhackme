# Linux Challenges Walkthrough

              |                     |
--------------|---------------------|
Date          | 2020-05-31          |
Learning Path | Complete Beginner   |
Box           | Linux Challenge     |

## 1) Introduction (init access)

>Username: garry
>Password: letmein

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

### Notes

**cron** is the name of tool, **crontab** is the *file* that lists the jobs that **cron** executes --and those jobs are called, **cronjobs**.  // Note: file locations vary by OS.

**/etc directory** contains *system-wide configuration files* that are editable administrator.  // Note: *user-specific config files* are located in each user's **/home directory**.

the **hosts** file is an OS file that **maps hostnames to IP addresses** in plain text (.txt).

tool                     | description   |
-------------------------|---------------|
grep **\\b**             | stands for *boundary* ~= beginning of a word.  Can use either double backslash or '\b'. |
tar -x, --extract, --get | extract files from an archive        |
tar -v, --verbose        | verbosely list files processed       |
tar -f, --file ARCHIVE   | use archive file or device ARCHIVE   |
ps -a                    | show 'a'll processes for 'a'll users |
ps -u                    | show 'u'ser/owner of the processes   |
ps -x                    | show unattached terminal processes   |


## 3) Linux Functionality


## 4) Data Representation, Strings, and Premissions


## 5) SQL, FTP, Groups, and RDP




