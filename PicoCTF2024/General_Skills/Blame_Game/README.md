# Blame Game - General Skills

## Description

Someone's commits seems to be preventing the program from working. Who is it? You can download the challenge files here:

- [challenge.zip](./challenge.zip)

#### Hints:

- In collaborative projects, many users can make many changes. How can you see the changes within one file?
- Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control).
- You can use `python3 <file>.py` to try running the code, though you won't need to for this challenge.

## Solution

We are given a zip file [`challenge.zip`](./challenge.zip) which when extracted creates a "drop-in" directory with a single file `message.py` containing the following...

```python
print("Hello, World!"
```

On viewing all files, we see that this is a git repository.

```bash
$ ls -al
total 16
drwxr-xr-x 3 admin admin 4096 Mar 12 05:37 .
drwxr-xr-x 3 admin admin 4096 Jun 10 20:31 ..
drwxr-xr-x 8 admin admin 4096 Jun 10 20:38 .git
-rw-r--r-- 1 admin admin   22 Mar 12 05:37 message.py
```

But on viewing the logs, there seem to be multiple commits with similar commit message and no changes in the repository at all. I tried to hard reset to a random commit but there was no change in the files.

```bash
$ git log                                                                              
commit 572ef8669e27c6c3cb78e98733405c3c210b0b8b (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:13 2024 +0000

    important business work

commit 78695a92b83a9b930b0d1da98e063269dbd7ebd4
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:13 2024 +0000

    important business work

commit d95a880b37c264d783c631886b9ddebfddcde9ea
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:13 2024 +0000

    important business work

commit 96702f500fa04883ac91829f3b19cf65c3efd8e7
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:13 2024 +0000

    important business work

commit 7730397f0bc614b3e0bc198d19b53c24b11fc94f
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:13 2024 +0000

    important business work
```

I tried to view one of the initial commits using the `tail` command and the flag was revealed.

```bash
$ git log | tail -20

    important business work

commit 6f9f8fc8907eefb90424f81d659f717c5c0b2c8a
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:11 2024 +0000

    important business work

commit 8c83358c32daee3f8b597d2b853c1d1966b23f0a
Author: picoCTF{@sk_th3_1nt3rn_2c6bf174} <ops@picoctf.com>
Date:   Tue Mar 12 00:07:11 2024 +0000

    optimize file size of prod code

commit caa945839a2fc0fb52584b559b4e89ac7c46bf54
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:11 2024 +0000

    create top secret project
```
