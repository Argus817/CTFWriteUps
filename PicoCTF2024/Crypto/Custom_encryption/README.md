# Custom encryption - Crypto

## Description

Can you get sense of this code file and write the function that will decode the given encrypted file content. <br>Find the encrypted file here [flag_info](./enc_flag) and [code file](./custom_encryption.py) might be good to analyze and get the flag.

#### Hints:

- Understanding encryption algorithm to come up with decryption algorithm.

#### Attachments: [`enc_flag`](./enc_flag) and [`custom_encryption.py`](./custom_encryption.py)

## Solution

We are given a text file [`enc_flag`](./enc_flag) which looks like the following...

```
a = 95
b = 21
cipher is: [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
```

We are also given a python script file [`custom_encryption.py`](./custom_encryption.py) which looks like the following...

```python
from random import randint
import sys

def generator(g, x, p):
    return pow(g, x) % p

def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher

def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True

def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')

if __name__ == "__main__":
    message = sys.argv[0]
    print(message)
    test(message, "trudeau")
```

The contents of the text file [`enc_flag`](./enc_flag) is definitely the output of the above python code. Which means I only need to reverse engineer the code to create a decryption script. On further analysing the code, I realised we already have all the information to generate the key and reverse engineer each function.

The complete decryption script is implemented in [`solve.py`](./solve.py). On executing the code, we get the flag...

```bash
$ python3 solve.py
picoCTF{custom_d2cr0pt6d_66778b34}
```
