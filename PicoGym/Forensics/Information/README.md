# Information - Forensics

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

#### Hints:

- Look at the details of the file

#### Attachments: [`cat.jpg`](./cat.jpg)

## Solution

We are given an image file [`cat.jpg`](./cat.jpg)

![cat.jpg](./cat.jpg)

There seems to be nothing out of the ordinary after looking at the image. `binwalk` confirms it.

```bash
binwalk cat.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
```

So there may be something hidden in the metadata of the image. Using the linux command `exiftool`, I uncovered the following...

```bash
$ exiftool cat.jpg 
ExifTool Version Number         : 12.76
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2024:06:04 13:35:08+05:30
File Access Date/Time           : 2024:06:04 13:35:33+05:30
File Inode Change Date/Time     : 2024:06:04 13:35:08+05:30
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

The licence value could be a *base64* value. After decoding, we get the following...

```bash
$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d
picoCTF{the_m3tadata_1s_modified}
```

Hence the flag is `picoCTF{the_m3tadata_1s_modified}`.
