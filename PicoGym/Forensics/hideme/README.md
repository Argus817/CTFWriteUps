# hideme - Forensics

## Description

Every file gets a flag. 

The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](./flag.png).

#### Attachments: [`flag.png`](./flag.png)

## Solution

We are given a normal looking image file [`flag.png`](./flag.png). Using `file` command confirms it. It looks like below...

![image](./flag.png)

```bash
$ file flag.png
flag.png: PNG image data, 512 x 504, 8-bit/color RGBA, non-interlaced
```

Using the `binwalk` command on the file produced some interesting results.

```bash
$ binwalk flag.png   

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2997, uncompressed size: 3152, name: secret/flag.png
43036         0xA81C          End of Zip archive, footer length: 22
```

Hence I used `binwalk` to extract the hidden directory [`secret`](./_flag.png.extracted/secret).

```bash
$ binwalk flag.png -e
```

The hidden directory contained an image file [`flag.png`](_flag.png.extracted/secret/flag.png).

![image](_flag.png.extracted/secret/flag.png)

Hence, the flag is `picoCTF{Hiddinng_An_imag3_within_@n_ima9e_85e04ab8}`.
