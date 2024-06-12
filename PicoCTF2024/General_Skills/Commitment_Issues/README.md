# Commitment Issues - General Skills

## Description

I accidentally wrote the flag down. Good thing I deleted it! You download the challenge files here:

- [challenge.zip](./challenge.zip)

#### Hints:

- Version control can help you recover files if you change or lose them!
- Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control)
- You can 'checkout' commits to see the files inside them

#### Attachments: [`challenge.zip`](./challenge.zip)

## Solution

We are given a zip file [`challenge.zip`](./challenge.zip) which when extracted creates a "drop-in" directory with a single file `message.txt` containing the following...

```
TOP SECRET
```

Now there doesn't seem to be any clue on how to get the flag but when I tried to list all files in the directory, things got a little interesting.

```bash
$ ls -al
total 16
drwxr-xr-x 3 admin admin 4096 Mar 12 05:36 .
drwxr-xr-x 3 admin admin 4096 Jun 10 15:12 ..
drwxr-xr-x 8 admin admin 4096 Mar 12 05:36 .git
-rw-r--r-- 1 admin admin   11 Mar 12 05:36 message.txt
```

The directory turned out to be a git repository. This means there may be previous commits containing the flag. My suspicions turned out to be correct after viewing the logs. There existed a single previous commit with the commit message "create flag". The flag is revealed after a hard reset on the repository.

```bash
$ git log   
commit 42942c9c605b30100f5d859ef6e172027447c0db (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    remove sensitive info

commit b562f0b425907789d11d2fe2793e67592dc6be93
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    create flag

$ git reset b562f0b425907789d11d2fe2793e67592dc6be93 --hard
HEAD is now at b562f0b create flag

$ git log                                                  
commit b562f0b425907789d11d2fe2793e67592dc6be93 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:06:23 2024 +0000

    create flag

$ git status
On branch master
nothing to commit, working tree clean

$ ls -al
total 16
drwxr-xr-x 3 admin admin 4096 Jun 10 15:36 .
drwxr-xr-x 3 admin admin 4096 Jun 10 15:12 ..
drwxr-xr-x 8 admin admin 4096 Jun 10 15:36 .git
-rw-rw-r-- 1 admin admin   27 Jun 10 15:36 message.txt

$ cat message.txt
picoCTF{s@n1t1z3_c785c319}
```
