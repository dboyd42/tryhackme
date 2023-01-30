# Hacking with Powershell

> Author: David Boyd<br>
> Date:  2023-01-25

## Task 1: Objectives

``` bash
$AM_USER1='Administrator'
$AM_PASS1='BHN2UVw0Q'
```

## Task 2: What is Powershell?

**Powershell**<br>
&nbsp;&nbsp;- is the Windows OOP Scripting Language & shell environment built
using the .NET framework.

**cmdlets**<br>
&nbsp;&nbsp;- are Powershell commands that output objects

**Syntax:** `Verb-Noun` :arrow_right: ie. `Get-Command`

Common verbs:

- `Get`
- `Start`
- `Stop`
- `Read`
- `Write`
- `New`
- `Out`

Full **Verb** list [here](https://docs.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7).

### Q&A

**1. What is the command to get help about a particular cmdlet (without any
parameters)?**

> `Get-Help`

## Task 3: Basic Powershell Commands

Useful commands:

- `Get-Command` and `Get-Help`

### The `Get-Help` Command

| `Get-Help` | Description                      |
|------------|----------------------------------|
| Syntax     | `Get-Help <Cmd-Name> -<Params>`  |
| @params    | `-Examples`                      |
| Example    | `Get-Help Get-Command -Examples` |

### The `Get-Command` Command

| `Get-Command`              | Description                                  |
|----------------------------|----------------------------------------------|
| Syntax w/ Pattern Matching | `Get-Command Verb-*`<br>`Get-Command *-Noun` |
| Example                    | `Get-Command New-*`                          |

### Object Manipulation

The **Pipeline (`|`)** is used to pass the cmdlet's object to the next cmdlet
(unlike other shells that pass strings to the cmd after the pipe).  Each cmdlet
object contains *methods* and *properties*.

**Syntax:** `Verb-Noun | Get-Member`<br>
**Example:** `Get-Command | Get-Member -MemberType Method`

### Creating Objects from Previous *cmdlets*

`Select-Object`<br>
&nbsp;&nbsp;- Extract the property from a cmdlet's output  and create a new object.

**Example:** `Get-ChildItem | Select-Object -Property Mode, Name`

`Mode`<br>
&nbsp;&nbsp;- a Get-ChildItem's cmdlet property that displays the files'
permissions.

:X: You can also use the following flags to select particular information:

- `first` - gets the first `x` object
- `last` - get the last `x` object
- `unique` - shows the unique objects
- `skip` - skips `x` objects

### Filtering Objects

`Where-Object`<br>
&nbsp;&nbsp;- filters output objects to match a specific value.

**Syntax1:** `Verb-Noun | Where-Object -Property PropertyName -operator
Value`<br>
**Syntax2:** `Verb-Noun | Where-Object {$_.PropertyName -operator Value}`

`$_` operator<br>
&nbsp;&nbsp;- used to iterate through every object passed to the cmdlet

`-operator` values:

- `-Contains` - if any item in the property value is an exact match for x value
- `-eq` - if the property value is the same as the specified value
- `-gt` - if the property value is greater than the specified value
- `-Match`

Full `operator` list [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-6)

**Example:**
``` powershell
# Get stopped processes
Get-Service | Where-Object -Property Status -eq Stopped
```

### Sort Object

`Sort-Object`<br>
&nbsp;&nbsp;- sort to extract information more efficiently.

**Syntax:** `Verb-Noun | Sort-Object`<br>
**Example:** `Get-ChildItem | Sort-Object`

### Q&A

**1. What is the location of the file "interesting-file.txt"?**

`Get-ChildItem -Path C:\ -Recurse | Where-Object -Property Name -eq
interesting-file.txt`

- :warning: The filename "interesting-file.txt" is not the full name.
- :x: Operator `-Contains` did not find file
- :heavy_check_mark: Operator `-Match` found file using wildcards

> `Get-ChildItem -Path C:\ -Recurse -File -ErrorAction SilentlyContinue |
Where-Object {$_.Name -Match ".*interesting*"}`
>> **ANSWER:** C:\Program Files

**2. Specify the contents of this file.**

> Get-Content "C:\Program Files\interesting.txt.txt"
>> **ANSWER:** notsointerestingcontent

**3. How many cmdlets are installed on the system (only cmdlets, not functions
and aliases)?**

*Hint 1: `Get-Help Get-Command`<br>*
*Hint 2: `Measure-Object`*

> Get-Command -CommandType Cmdlet | Measure-Object -Line
>> **ANSWER:** 6638

**4. Get the MD5 hash of the interesting-file.txt**

> Get-FileHash -Algorithm MD5 "C:\Program Files\interesting.txt.txt" | fl *
>> **ANSWER:** 49A586A2A9456226F8A1B4CEC6FAB329

**5. What is the command to get the current working directory?**

> Get-Alias pwd
>> **Answer:** Get-Location

**6. Does the path "C:\Users\Administrator\Documents\Passwords" Exist(Y/N)?**

> Get-ChildItem -Attributes Hidden
>> **ANSWER:** N

**7. What command would you use to make a request to a web server?**

> Get-Alias curl; Get-Alias wget
>> **ANSWER:** Invoke-WebRequest

**8. Base64 decode the file b64.txt on Windows.**

*Hint: It's an unnecessarily long command...*

> Get-Content C:\Users\Administrator\Desktop\b64.txt |
> %{[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($_))}
>> **ANSWER:** ihopeyoudidthisonwindows

## Task 4: Enumeration

## Task 5: Basic Scripting Challenge

## Task 6: Intermediate Scripting
