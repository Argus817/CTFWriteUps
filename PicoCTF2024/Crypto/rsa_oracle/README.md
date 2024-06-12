# rsa_oracle - Crypto

## Description

Can you abuse the oracle? <br>An attacker was able to intercept communications between a bank and a fintech company. They managed to get the [message](./secret.enc) (ciphertext) and the [password](./password.enc) that was used to encrypt the message. <br>After some intensive reconassainance they found 
out that the bank has an oracle that was used to encrypt the password 
and can be found here `nc <host> <port>`. Decrypt the password and use it to decrypt the message. The oracle can decrypt anything except the password.

#### Hints:

- Crytography Threat models: chosen plaintext attack.
- OpenSSL can be used to decrypt the message. e.g openssl enc -aes-256-cbc -d ...
- The key to getting the flag is by sending a custom message to the server by taking advantage of the RSA encryption algorithm.The key to getting the flag is by sending a custom message to the server by taking advantage of the RSA encryption algorithm.
- Minimum requirements for a useful cryptosystem is CPA security.

#### Attachments: [`secret.enc`](./secret.enc) and [`password.enc`](./password.enc)

## Solution

We are given a file [`secret.enc`](./secret.enc) containing some encoded data which cannot be viewed and a file [`password.enc`](./password.enc) containing an RSA encoded password, as given in the description. The password file looks like the following...

```
1634668422544022562287275254811184478161245548888973650857381112077711852144181630709254123963471597994127621183174673720047559236204808750789430675058597
```

Given that the oracle at `<host>` and `<port>` was used to encrypt the password and it can also be used to encrypt or decrypt any arbitrary data provided by the user, it is evident we have to use the Chosen Plaintext Attack.

Let public key $n$, $e$, and private key exponent $d$. We are given ciphertext $c_p$ corresponding to password $p$. Hence $c_p \equiv (p)^e \ (mod\ n)$ and $p\equiv(c_p)^d\ (mod\ n)$. We can't directly send $c_p$ to the oracle for decryption so we need to change it. We first send $p_2 = 2$ for encryption and receive $c_2\equiv(2)^e\ (mod\ n)$. Also $(c_2)^d\equiv2\ (mod\ n)$. Next we send payload $\equiv c_p*c_2\ (mod\ n)$ for decryption which gives us $(c_p*c_2)^d\ (mod\ n)\equiv(c_p)^d*(c_2)^d\ (mod\ n)\equiv p*2 \ (mod\ n)$.

Therefore now we have $p$ as the decrypted password and the required flag encrypted in [`secret.enc`](./secret.enc). Hence an OpenSSL command to decrypt the file will suffice.

The entire solution code is implemented in [`solve.py`](./solve.py). It would only run in Linux which has OpenSSL installed.

```bash

```
