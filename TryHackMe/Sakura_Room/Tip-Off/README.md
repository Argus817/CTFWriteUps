# Tip-Off

## Description

### Background

The OSINT Dojo recently found themselves the victim of a cyber attack. It seems that there is no major damage, and there does not appear to be any other significant indicators of compromise on any of our systems. However during forensic analysis our admins found an image left behind by the cybercriminals. Perhaps it contains some clues that could allow us to determine who the attackers were? 

We've copied the image left by the attacker, you can view it in your browser [here](https://raw.githubusercontent.com/OsintDojo/public/3f178408909bc1aae7ea2f51126984a8813b0901/sakurapwnedletter.svg).

### Instructions

Images can contain a treasure trove of information, both on the surface as well as embedded within the file itself. You might find information such as when a photo was created, what software was used, author and copyright information, as well as other metadata significant to an investigation. In order to answer the following question, you will need to thoroughly analyze the image found by the OSINT Dojo administrators in order to obtain basic information on the attacker.

#### Answer the questions below

What username does the attacker go by?

## Solution

We are given an SVG file [sakurapwnedletter.svg](./sakurapwnedletter.svg). It is a normal SVG file as confirmed by the `file` command. It looks like the following...

![sakurapwnedletter.svg](./sakurapwnedletter.svg)

 Using the `binwalk` command produces some interesting results.

```bash
$ file sakurapwnedletter.svg 
sakurapwnedletter.svg: SVG Scalable Vector Graphics image

$ binwalk sakurapwnedletter.svg                                  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             XML document, version: "1.0"
766           0x2FE           Unix path: "/home/SakuraSnowAngelAiko/Desktop/pwnedletter.png"
709732        0xAD464         Unix path: "/home/sin/Desktop/OSINTDOJO/osintdojosticker.png"
```

We have 2 Unix paths, the second one seems to belong to OSINT Dojo as it has a directory `OSINTDOJO` on the Desktop. The first path should belong to the attacker's home directory. It also contains the `pwnedletter.svg` which was left behind by the attacker.

#### Answer

`SakuraSnowAngelAiko`
