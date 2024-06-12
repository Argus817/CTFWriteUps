# C3 - Crypto

## Description

This is the Custom Cyclical Cipher! <br>Download the ciphertext [here](./ciphertext). <br>Download the encoder [here](./convert.py). <br>Enclose the flag in our wrapper for submission. If the flag was "example" you would submit "picoCTF{example}".

#### Hints:

- Modern crypto schemes don't depend on the encoder to be secret, but this one
  does.

#### Attachments: [`ciphertext`](./ciphertext) and [`convert.py`](./convert.py)

## Solution

We are give a text file [`ciphertext`](./ciphertext) which looks like the following...

```
DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl
```

We are also given a python script [`convert.py`](./convert.py) which looks like the following...

```python
import sys
chars = ""
from fileinput import input
for line in input():
  chars += line

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

out = ""

prev = 0
for char in chars:
  cur = lookup1.index(char)
  out += lookup2[(cur - prev) % 40]
  prev = cur

sys.stdout.write(out)
```

The contents of the text file must be the output of the above code. So I wrote a reverse code in [`solve.py`](./solve.py) and executed it with the text file as the input.

```bash
$ python3 solve.py
#asciiorder
#fortychars
#selfinput
#pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1
```

The output turned out to be a python 2 code. It had two interesting comments `#selfinput` and `#pythontwo`. I figured I could feed this code to itself during its execution. I was right and the flag was revealed.

```bash
$ python3 solve.py > plaincode

$ cat plaincode | python2 plaincode
a
d
l
i
b
s
```

Hence the flag is `picoCTF{adlibs}`
