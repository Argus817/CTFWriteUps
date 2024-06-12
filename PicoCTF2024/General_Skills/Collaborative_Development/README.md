# Collaborative Development - General Skills

## Description

My team has been working very hard on new features for our flag printing program! I wonder how they'll work together? You can download the challenge files here:

- [challenge.zip](./challenge.zip)

#### Hints:

- `git branch -a` will let you see available branches
- How can file 'diffs' be brought to the main branch? Don't forget to `git config`!
- Merge conflicts can be tricky! Try a text editor like nano, emacs, or vim.

## Solution

We are given a zip file [`challenge.zip`](./challenge.zip) which when extracted creates a "drop-in" directory with a single file `flag.py` containing the following...

```python
print("Printing the flag...")
```

On viewing all files, we see that this is a git repository.

```bash
$ ls -al
total 16
drwxr-xr-x 3 admin admin 4096 Mar 12 05:37 .
drwxr-xr-x 3 admin admin 4096 Jun 10 21:24 ..
drwxr-xr-x 8 admin admin 4096 Mar 12 05:37 .git
-rw-r--r-- 1 admin admin   30 Mar 12 05:37 flag.py
```

On viewing the logs, we see that there exists only one commit in the current branch.

```bash
$ git log           
commit 2258a0f267d57e8b6025e2a020b77fac7a553c92 (HEAD -> main)
Author: picoCTF <ops@picoctf.com>
Date:   Tue Mar 12 00:07:54 2024 +0000

    init flag printer
```

I tried checking if there existed some other branch in the repository and I was right. There were 3 branches other than main. I switched to one of them and found a part of the flag.

```bash
$ git branch
  feature/part-1
  feature/part-2
  feature/part-3
* main

$ git switch feature/part-1 
Switched to branch 'feature/part-1'

$ lla
total 16
drwxr-xr-x 3 admin admin 4096 Jun 10 21:34 .
drwxr-xr-x 3 admin admin 4096 Jun 10 21:29 ..
drwxr-xr-x 8 admin admin 4096 Jun 10 21:34 .git
-rw-rw-r-- 1 admin admin   64 Jun 10 21:34 flag.py

$ cat flag.py
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')
```

I figured the other parts of the flag must be in the other branches.

```bash
$ git switch feature/part-2 
Switched to branch 'feature/part-2'

$ cat flag.py
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')    

$ git switch feature/part-3
Switched to branch 'feature/part-3'

$ cat flag.py              
print("Printing the flag...")

print("w0rk_6c06cec1}")
```

Hence I have my flag `picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_6c06cec1}`
