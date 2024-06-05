from PIL import Image
import string
import os

img = Image.open('Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png')
pixels = img.load()
w, h = img.size

def readMSB():
    binary = ""
    for y in range(h):
        for x in range(w):
            for i in pixels[x, y]:
                binary += str(i >> 7)
    output = ""
    for i in range(int(len(binary)/8)):
        output += chr(int(binary[i*8: i*8+8], 2))
    return output

def saveOutput(content):
    printable = set(string.printable)
    content = "".join(filter(lambda x: x in printable, content))
    with open('output', "w") as f:
        f.write(content)

output = readMSB()
printable = set(string.printable)
output = "".join(filter(lambda x: x in printable, output))

for line in output.split("\n"):
    if 'picoCTF{' in line:
        print(line.strip())
        break