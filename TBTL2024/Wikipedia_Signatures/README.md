# Wikipedia Signatures - Crypto

## Hint

https://en.wikipedia.org/w/index.php?title=Digital_signature&oldid=1113936031 <br>
Alice signs a message—"Hello Bob!"—by appending to the original message a version encrypted with her private key. Bob receives both the message and signature. He uses Alice's public key to verify the authenticity of the message, i.e. that the encrypted copy, decrypted using the public key, exactly matches the original message.<br> 
`nc <hostname> <port>`

#### Attachments: [`server.py`](./server.py)

## Solution

We are given a [`server.py`](./server.py) file which includes code running on the remote host. Its contents are as follows... <br>

```python3
#!/usr/bin/python3

from redacted import FLAG

from Crypto.Util.number import bytes_to_long
from Crypto.Math.Numbers import Integer
from Crypto.PublicKey import RSA

import signal


TARGET = b'I challenge you to sign this message!'


def myprint(s):
    print(s, flush=True)


def handler(_signum, _frame):
    myprint("Time out!")
    exit(0)


def rsa(m, n, x):
    if not 0 <= m < n:
        raise ValueError("Value too large")
    return int(pow(Integer(m), x, n))


# Alice signs a message—"Hello Bob!"—by appending to the original 
# message a version encrypted with her private key. 
def wikipedia_sign(message, n, d):
    return rsa(message, n, d)


# Bob receives both the message and signature. He uses Alice's public key 
# to verify the authenticity of the message, i.e. that the encrypted copy,
# decrypted using the public key, exactly matches the original message.
def wikipedia_verify(message, signature, n, e):
    return rsa(signature, n, e) == bytes_to_long(message)


def main():
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(300)

    rsa_key = RSA.generate(1024)
    public_key = (rsa_key.n, rsa_key.e)

    myprint(f"RSA public key: {public_key}")
    myprint("Options:")
    myprint(f"1 <sig> -- Submit signature for {TARGET} and win")
    myprint("2 <msg> -- Sign any other message using wikipedia-RSA")

    for _ in range(10):
        line = input("> ")
        action, data = map(int, line.split())
        if action == 1:
            if wikipedia_verify(TARGET, data, rsa_key.n, rsa_key.e):
                myprint(f"{FLAG}")
                exit(0)
            else:
                myprint(f"Nope. Keep trying!") 
        elif action == 2:
            if data % rsa_key.n == bytes_to_long(TARGET):
                myprint(f"Nope. Won't sign that!") 
            else:
                sig = wikipedia_sign(data, rsa_key.n, rsa_key.d)
            myprint(sig)
        else:
            break


if __name__ == "__main__":
    main()
```

In this challenge, we need to create a digital signature of a fixed plaintext `TARGET` using the method how *textbook RSA signatures* are created. The server gives us the ability to ask for a signature of arbitrary plaintext and submit the signature of . It is clear we need to perform the chosen plaintext attack.

Given public key $n$, $e$ and  $p \equiv$ `TARGET`$\ (mod \ n)$ in integer form. Private key exponent $d$ is not given.<br>
The server won't let me input $p$ directly and get its signature ${s_p} \equiv (p)^d \ (mod\ n)$. Instead I asked the server to sign $(2p) \ (mod\ n)$ which the server has no issue in signing. I received the signature ${s_{2p}}\equiv(2p)^d \ (mod\ n)$. Next I calculated the inverse of $2$ which is $2^{-1} \ (mod\ n)$ and sent it to the server for signing. Hence I received the signature ${s_{2^{-1}}}\equiv {(2^{-1})^d}\ (mod\ n)$. Multiplying ${s_{2p}}$ and ${s_{2^{-1}}}$ would give me ${s_p}$ as we have <br>
${s_{2p}}\ ×\ {s_{2^{-1}}} \equiv (2p)^d \ (mod\ n)\ ×\ {(2^{-1})^d}\ (mod\ n) \equiv (\ (2p \ (mod\ n)) \ ×\  (2^{-1} \ (mod\ n))\ ) \ (mod\ n) \equiv p \ (mod\ n) \equiv s_p \ (mod\ n)$<br>
Hence $s_p \equiv {s_{2p}}\ ×\ {s_{2^{-1}}} \ (mod\ n)$ <br>
Now, obtaining the value of $s_p$, I submit the signature for the `TARGET` and win the flag.

Complete script to perform this attack is implemented in [`solve.py`](./solve.py).