s1="""abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

cat
mat
pat
bat

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+\

anilpara.com

321-555-4321
123.555.1234

Mr. Anil
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr.Anil
The cat sat on the mat
The caterpillar sat on the mat
Thecat sat on the mat"""
# print(s1)
import re
# print(r"\tAnil")
with open("urls.txt", mode='r') as fp:
    contents = fp.read()
    pattern = re.compile(r'https?://(www\.)?([a-z]+)(\.[a-z]*)')
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)


