# advanced-potion-making - Forensics

## Description

Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!

#### Attachments: [`advanced-potion-making`](./advanced-potion-making)

## Solution

We are given an unknown file [`advanced-potion-making`](./advanced-potion-making). `file` command is useless. As are `binwalk` and `exiftool` commands.

```bash
$ file advanced-potion-making
advanced-potion-making: data

$ binwalk advanced-potion-making  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
91            0x5B            Zlib compressed data, compressed

$ exiftool advanced-potion-making  
ExifTool Version Number         : 12.76
File Name                       : advanced-potion-making
Directory                       : .
File Size                       : 30 kB
File Modification Date/Time     : 2024:06:04 21:52:27+05:30
File Access Date/Time           : 2024:06:04 21:52:54+05:30
File Inode Change Date/Time     : 2024:06:04 21:52:40+05:30
File Permissions                : -rw-r--r--
Error                           : Unknown file type
```

Looking at the file signature using `hexedit`, we get the following...

```
00000000   89 50 42 11  0D 0A 1A 0A  00 12 13 14  49 48 44 52  .PB.........IHDR
00000010   00 00 09 90  00 00 04 D8  08 02 00 00  00 04 2D E7  ..............-.
00000020   78 00 00 00  01 73 52 47  42 00 AE CE  1C E9 00 00  x....sRGB.......
00000030   00 04 67 41  4D 41 00 00  B1 8F 0B FC  61 05 00 00  ..gAMA......a...
00000040   00 09 70 48  59 73 00 00  16 25 00 00  16 25 01 49  ..pHYs...%...%.I
00000050   52 24 F0 00  00 76 39 49  44 41 54 78  5E EC FD 61  R$...v9IDATx^..a
00000060   72 E3 4C 94  A6 59 CE 16  6A FE 76 CD  FE 57 D7 DD  r.L..Y..j.v..W..
00000070   5B 18 45 E9  4B 8A 7A 28  D1 9D 20 48  07 A9 63 76  [.E.K.z(.. H..cv
00000080   AC 2D 2B 3E  BF AF 5F 07  18 01 82 D7  B2 F3 FF F3  .-+>.._.........
00000090   FF FC 7F FF  7F 00 00 00  00 00 00 00  4B 18 58 02  ............K.X.
```

The file signature looked familiar to a PNG file. After reading on [Wikipedia](https://en.wikipedia.org/wiki/PNG) about PNG file specification, I had to change the data to PNG signature and supported IHDR values. The resulting data looked like the following, hence producing [`advanced-potion-making-1`](./advanced-potion-making-1).

```
00000000   89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  .PNG........IHDR
00000010   00 00 09 90  00 00 04 D8  08 02 00 00  00 04 2D E7  ..............-.
00000020   78 00 00 00  01 73 52 47  42 00 AE CE  1C E9 00 00  x....sRGB.......
00000030   00 04 67 41  4D 41 00 00  B1 8F 0B FC  61 05 00 00  ..gAMA......a...
00000040   00 09 70 48  59 73 00 00  16 25 00 00  16 25 01 49  ..pHYs...%...%.I
00000050   52 24 F0 00  00 76 39 49  44 41 54 78  5E EC FD 61  R$...v9IDATx^..a
00000060   72 E3 4C 94  A6 59 CE 16  6A FE 76 CD  FE 57 D7 DD  r.L..Y..j.v..W..
00000070   5B 18 45 E9  4B 8A 7A 28  D1 9D 20 48  07 A9 63 76  [.E.K.z(.. H..cv
00000080   AC 2D 2B 3E  BF AF 5F 07  18 01 82 D7  B2 F3 FF F3  .-+>.._.........
00000090   FF FC 7F FF  7F 00 00 00  00 00 00 00  4B 18 58 02  ............K.X.
```

The resultant image was entirely red...
![image](./advanced-potion-making-1)

After playing around in an image editor (GNU Image Manipulation Program), I tried an auto white balance function which was in-built into the program. It produced [advanced-potion-making-2](./advanced-potion-making-2) which shows us the flag...

![image](./advanced-potion-making-2)

Hence the flag is `picoCTF{w1z4rdry}`.
