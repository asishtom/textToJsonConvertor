#{      “firstName”: “Lakshya”, “middleName”: “Shiv”, “middleName”: “Rama”, “lastName”: “Krishnan”, “fullName”: “Lakshya Shiv Rama Krishnan”}
import os
import sys
import fileinput
import json

print("String To Cleam:")
cc = input(">")
print("String replace it with:")
rc = input(">")
print("File to  Clean:")
fts = input(">")
temp = open(fts, 'r+')
opf=open('data.json', 'w')
for line in fileinput.input(fts):
    words = line.split(sep='.')
    if words[0].__contains__('\x00\n'):  # != '\x00\n' and words[0] != '\x00Y\x00i\x00s\x00h\x00u\x00\n' :
        pass
    else:
        if words.__len__() >= 2:
            temp.write(line.replace(cc, rc))

