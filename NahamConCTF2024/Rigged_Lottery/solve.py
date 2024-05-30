from pwn import *

with open("data", 'r') as file:
    data = [[j.encode() for j in i.strip().split(' ')] for i in file.readlines()]

def main():
    target = process("./server.py")
    #target = remote("challenge.nahamcon.com",32629)

    target.recv()
    target.sendline(b"35")
    for i in data:
        for j in i:
            target.recv()
            target.sendline(j)
    target.recvuntil(b"well-deserved flag --> ")
    print(f"Flag: {target.recv().decode().strip()}")

if __name__ == "__main__":
    main()
