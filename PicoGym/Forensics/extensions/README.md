# extensions - Forensics

## Description

This is a really weird text file [TXT](./flag.txt)? Can you find the flag?

#### Hints:

- How do operating systems know what kind of file it is? (It's not just the ending!)

#### Attachments: [`flag.txt`](./flag.txt)

## Solution

We are given an unopenable file [`flag.txt`](./flag.txt). The `file` command says that it is a png file.

```bash
$ file flag.txt                                               
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

This is confirmed by viewing the file signature of the file using `hexedit`. It matches with the PNG file signature.

```
00000000   89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  .PNG........IHDR
00000010   00 00 06 A1  00 00 02 60  08 02 00 00  00 85 AD 5E  .......`.......^
00000020   9A 00 00 00  01 73 52 47  42 00 AE CE  1C E9 00 00  .....sRGB.......
00000030   00 04 67 41  4D 41 00 00  B1 8F 0B FC  61 05 00 00  ..gAMA......a...
00000040   00 09 70 48  59 73 00 00  16 25 00 00  16 25 01 49  ..pHYs...%...%.I
00000050   52 24 F0 00  00 26 95 49  44 41 54 78  5E ED DD 6B  R$...&.IDATx^..k
00000060   42 1B 39 B7  05 D0 3B 2E  06 94 F1 30  9A 4C 26 83  B.9...;....0.L&.
00000070   F9 AE 5F 80  4E 3D 25 BB  4C B3 F1 5A  BF BA A1 4A  .._.N=%.L..Z...J
00000080   75 74 24 13  79 27 C0 FF  FD 0F 00 00  00 00 48 26  ut$.y'........H&
00000090   E3 03 00 00  00 80 6C 32  3E 00 00 00  00 C8 26 E3  ......l2>.....&.
```

Hence, only changing the extension of the file from `.txt` to `.png` would suffice, producing [`flag.png`](./flag.png). It looks like the following...

![image](./flag.png)

Hence, the flag is `picoCTF{now_you_know_about_extensions}`
