# interencdec - Crypto

## Description

Can you get the real meaning from this file. <br>Download the file [here](./enc_flag).

#### Hints:

- Engaging in various decoding processes is of utmost importance

#### Attachments: [enc_flag](./enc_flag)

## Solution

We are given a text file with a single line of text. It's contents are the following...

```
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzJhMnd6TW1zeWZRPT0nCg==
```

It looks like a base64 text. On decoding it, we get another base64 text, which after decoding we get a rubbish text which almost looks like the flag as special characters are at the same place.

```bash
$ cat enc_flag | base64 -d                                        
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ=='

$ echo d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg2a2wzMmsyfQ== | base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}
```

I figured out it must be a simple shift cipher so I tried all character shifts of the Caesar cipher on https://cryptii.com/pipes/caesar-cipher . I found the flag on a character shiift of 7.

Hence the flag was found to be `picoCTF{caesar_d3cr9pt3d_86de32d2}`.

**Note: The flag is different for different users on PicoCTF**
