from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

target = process("./server.py")
#target = remote(hostname, port)   #Using hostname and port given in challenge

target.recvuntil(b"public key: ")
(n,e) = eval(target.recvuntil(b"\n")[:-1].decode())
target.recvuntil(b"signature for ")
TARGET = eval(target.recvuntil(b"!'").decode())

target.recv()
target.sendline(b"2 "+str(bytes_to_long(TARGET)*2).encode())
c = int(target.recv()[:-3].decode())
#print(f"c = {c}")

twoinv = pow(2,-1,n)
target.sendline(b"2 "+str(twoinv).encode())
x = int(target.recv()[:-3].decode())
#print(f"x = {x}")

T = (c*x)%n
target.sendline(b"1 "+str(T).encode())
print("flag:",target.recv()[:-1].decode())
target.close()
