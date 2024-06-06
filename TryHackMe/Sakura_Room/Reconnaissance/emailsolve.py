import string
from base64 import b64decode as dec

with open('publickey','r') as f:
    lines = [i.strip() for i in f.readlines()][1:-1]

output = ""
for line in lines:
    output += line
output = dec(output)
printable = set(string.printable.encode())
output = "".join([chr(i) for i in list(filter(lambda x: x in printable, output))])
print(output)
