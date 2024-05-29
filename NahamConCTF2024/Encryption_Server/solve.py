from pwn import *
from sage.all import *

target = process("./RSA_Encryption_Server.py")
#target = remote("challenge.nahamcon.com",32375)
flag = ""

target.recv()
target.sendline(b"1")
target.recv()
target.sendline(b"\x02")
target.recvuntil(b"message:\n> [")
e = int((log(Integer(int(target.recvuntil(b"]")[:-1])))/log(Integer(2))))
target.recv()
def getEncFlag():
    target.sendline(b"2")
    target.recvuntil(b"chosen N:\n> ")
    n = int(target.recvuntil(b"\n")[:-1])
    target.recvuntil(b"message:\n> ")
    c = eval(target.recvuntil(b"]"))
    target.recv()
    return (c,n)

(c1,n1) = getEncFlag()
(c2,n2) = getEncFlag()
(c3,n3) = getEncFlag()
(c4,n4) = getEncFlag()

R1 = Zmod(n1)
R2 = Zmod(n2)
R3 = Zmod(n3)
R4 = Zmod(n4)

n = len(c1)  #flag length = n

for i in range(n):
    t1 = Integer(c1[i]) * (Integer(n2)*Integer(n3)*Integer(n4)) * Integer(R1(Integer(n2)*Integer(n3)*Integer(n4))**Integer(-1))
    t2 = Integer(c2[i]) * (Integer(n1)*Integer(n3)*Integer(n4)) * Integer(R2(Integer(n1)*Integer(n3)*Integer(n4))**Integer(-1))
    t3 = Integer(c3[i]) * (Integer(n2)*Integer(n1)*Integer(n4)) * Integer(R3(Integer(n2)*Integer(n1)*Integer(n4))**Integer(-1))
    t4 = Integer(c4[i]) * (Integer(n2)*Integer(n1)*Integer(n3)) * Integer(R4(Integer(n2)*Integer(n1)*Integer(n3))**Integer(-1))
    

    R = Zmod(n1*n2*n3*n4)
    c = Integer(R(t1+t2+t3+t4))
    #print( f"Assertion: {int(R1(c)) == c1[i]}")
    #print( f"Assertion: {int(R2(c)) == c2[i]}")
    #print( f"Assertion: {int(R3(c)) == c3[i]}")
    #print( f"Assertion: {int(R4(c)) == c4[i]}")
    m = c**(Integer(1)/Integer(e))
    #print(int(m))
    flag += chr(int(m))

print(f"Flag: {flag}")
