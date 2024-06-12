# Time Machine - General Skills

## Description

What was I last working on? I remember writing a note to help me remember... You can download the challenge files here:

- [challenge.zip](./challenge.zip)

#### Hints:

- The `cat` command will let you read a file, but that won't help you here!

- Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control).

- When committing a file with git, a message can (and should) be included.

#### Attachments: [`challenge.zip`](./challenge.zip)

## Solution

We are given a zip file [`challenge.zip`](./challenge.zip) which when extracted  creates a "drop-in" directory which is found to be a git repository after looking at hidden files.

```bash
$ ls -al
total 16
drwxr-xr-x 3 admin admin 4096 Mar 12 05:37 .
drwxr-xr-x 3 admin admin 4096 Jun 10 15:52 ..
drwxr-xr-x 8 admin admin 4096 Mar 12 05:37 .git
-rw-r--r-- 1 admin admin   87 Mar 12 05:37 message.txt

$ cat message.txt
This is what I was working on, but I'd need to look at my commit history to know why...
```

A quick look at the logs reveals the flag right there in the commit message.

```bash
$ git log   
commit 712314f105348e295f8cadd7d7dc4e9fa871e9a2 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:26 2024 +0000

    picoCTF{t1m3m@ch1n3_e8c98b3a}
```
