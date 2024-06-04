# Matryoshka doll - Forensics

## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](./dolls.jpg)

#### Hints

- Wait, you can hide files inside files? But how do you find them?

#### Attachments: [`dolls.jpg`](./dolls.jpg)

## Solution

We are given an image file [`dolls.jpg`](./dolls.jpg)

![dolls.jpg](dolls.jpg)

The image looks nothing out of the ordinary. Using `binwalk` we get the following...

```bash
$ binwalk dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22
```

Hence we know there is a file hidden inside this image, which is confirmed by the hint given. Using `binwalk` to extract the file, we get another image of a doll ([`2_c.jpg`](./_dolls.jpg.extracted/base_images/2_c.jpg)) inside [`_dolls.jpg.extracted`](./_dolls.jpg.extracted) directory.

```bash
binwalk dolls.jpg -e

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378942, uncompressed size: 383937, name: base_images/2_c.jpg
651600        0x9F150         End of Zip archive, footer length: 22
```

This doll is slightly smaller than the above image. This must be a similer situation like a Matryoshka doll where files are recursively hidden inside images. My suspicions are confirmed when I extract hidden files from [`2_c.jpg`](./_dolls.jpg.extracted/base_images/2_c.jpg). I get another image [`3_c.jpg`](./_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/3_c.jpg), and then [`4_c.jpg`](./_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/4_c.jpg) and then finally I get the flag in a text file [`flag.txt`](./_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt). But the flag in the file contains some unwanted bytes. I used python to get rid of those unwanted characters. 

```python
>>> open("flag.txt",'rb').read()
b'p\x00i\x00c\x00o\x00C\x00T\x00F\x00{\x004\x00c\x00f\x007\x00a\x00c\x000\x000\x000\x00c\x003\x00f\x00b\x000\x00f\x00a\x009\x006\x00f\x00b\x009\x002\x007\x002\x002\x00f\x00f\x00b\x002\x00a\x003\x002\x00}'
>>> open("flag.txt",'rb').read().replace(b"\x00",b"")
b'picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}'
```

Hence the flag is `picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}`.