# Encryption Server - Cryptography
## Hint
I read online it's bad to re-use the prime numbers in RSA. So, I made this server that randomly generates them for me. <br>`nc <hostname> <port>`
#### Attachments: [`RSA_Encryption_Server.py`](./RSA_Encryption_Server.py)

## Solution
We are given a [`RSA_Encryption_Server.py`](./RSA_Encryption_Server.py) file which includes code running on the remote host. Its contents are as follows... <br>
```python3
#!/usr/bin/python3

from secrets import randbits
from sympy import nextprime
import random

e = random.randint(500,1000)

def encrypt(inp):
    p = nextprime(randbits(1024))
    q = nextprime(randbits(1024))
    n = p * q
    c = [pow(ord(m), e, n) for m in inp]
    return [n, c]

def main():
    
    while True:
        print('Welcome to the Really Shotty Asymmetric (RSA) Encryption Server!')
        print('1: Encrypt a message')
        print('2: View the encrypted flag')
        print('3: Exit')
        
        inp = ''
        while (not ('1' in inp or '2' in inp or '3' in inp)):
            inp = input('> ')
        
        if('3' in inp):
            print('Goodbye!')
            exit()

        elif('1' in inp):
            plain = input('Enter a message, and the server will encrypt it with a random N!\n> ')
            encrypted = encrypt(plain)

        elif('2' in inp):
            data = open('flag.txt', 'r').read()
            data = data.strip()
            encrypted = encrypt(data)

        print('Your randomly chosen N:')
        print(f'> {encrypted[0]}')
        print('Your encrypted message:')
        print(f'> {encrypted[1]}')
        print('\n')

if(__name__ == '__main__'):
    main()
```
In this challenge, the server is an encryption oracle which can encrypt any message using textbook RSA on each character. The other prompts include viewing the encrypted flag. The twist is that each time an encryption occurs, the RSA modulus $N$ is randomised. The only constant thing in the entire code is the exponent $e$ which is randomised at the beginning with bounds $500 \le e < 1000 $. From these bounds, the maximum value of $e$ can be $999$ and $2^{999} < N$. Hence $e$ can be obtained by sending a message `b"\x02"` to the encryption oracle and finding the logarithm of the encrypted result with base 2.

Next, the flag can be found by utilising the Chinese Remainder Theorem for each character of the flag. Given any character $c$ of the flag. Ciphertext of $c$ with RSA modulus $N_1$ will be $c^e \equiv a_1 \mod N_1$. Prompting the server to view the encrypted flag 4 times would give us 3 more datasets<br>
$c^e \equiv a_1 \mod N_1$ <br>
$c^e \equiv a_2 \mod N_2$ <br>
$c^e \equiv a_3 \mod N_3$ <br>
$c^e \equiv a_4 \mod N_4$ <br>

Chinese Remainder Theorem states that the above has a unique solution for modulus $N = N_1× N_2 × N_3 × N_4$. Using that, I found $c^e \equiv a \mod N$. Since $N = N_1× N_2 × N_3 × N_4$, meaning $N$ is a very large number. For any character $c$, $c^{999} < N_1× N_2 × N_3 × N_4$ and hence $c^e = a$. Hence $c$ can be found easily by finding $a^{\frac{1}{e}}$.

Complete solution is given in [`solve.py`](./solve.py). SageMath is used for better integer accuracy.

Mathematical procedure for finding $c^e \equiv a \mod N$ given the above data is as follows.<br>

$t_1 = a_1 × (N_2 × N_3 × N_4) × [(N_2 × N_3 × N_4)^{-1} \mod N_1]$ <br>
$t_2 = a_2 × (N_1 × N_3 × N_4) × [(N_1 × N_3 × N_4)^{-1} \mod N_2]$ <br>
$t_3 = a_3 × (N_2 × N_1 × N_4) × [(N_2 × N_1 × N_4)^{-1} \mod N_3]$ <br>
$t_4 = a_4 × (N_2 × N_3 × N_1) × [(N_2 × N_3 × N_1)^{-1} \mod N_4]$ <br>

$a = (t_1+t_2+t_3+t_4) \mod N$ where $N = N_1× N_2 × N_3 × N_4$