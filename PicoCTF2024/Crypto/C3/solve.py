with open("ciphertext", 'r') as cipherfile:
    cipher = cipherfile.read()

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

plain = ""
prev = 0
for char in cipher:
    y = lookup2.index(char)
    x = (y+prev)%40
    prev = x;
    plain += lookup1[x]
    
print(plain)