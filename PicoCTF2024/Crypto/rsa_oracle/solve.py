from pwn import remote
from Crypto.Util.number import long_to_bytes
import os

port = 49520

target = remote("titan.picoctf.net",port)

target.recv()
cp=int(open("password.enc",'r').read())

target.sendline(b"E")
target.recv()
target.sendline(b"\x02")
ct2 = int(target.recv()[59:-60].decode()) #ct

pay = cp*ct2
target.sendline(b"D")
target.recv()
target.sendline(str(pay).encode())
target.recvuntil(b"(c ^ d mod n): ")
pt2=int(target.recvuntil(b"\n")[:-1].decode(),16)
passwordpt = pt2//2
password = long_to_bytes(passwordpt).decode()
target.close()

print(f"Password: {password}")

#obtain flag by decrypting secret.enc using openssl
os.system("openssl enc -aes-256-cbc -d -in secret.enc -k "+password) #assuming the operating system is linux with openssl installed
