#{      “firstName”: “Lakshya”, “middleName”: “Shiv”, “middleName”: “Rama”, “lastName”: “Krishnan”, “fullName”: “Lakshya Shiv Rama Krishnan”}
import os
import sys
import fileinput
import json
print("Charactor To Cleam:")
cc = "\n"
print("Charactor replace it with:")
rc = ""
print("File to clean:")
fts = input(">")
temp = open(fts, 'r+')
opf=open('data.json', 'w')
for line in fileinput.input(fts):
    words = line.split(sep=' ')
    if words[0].__contains__('\x00\n'): #  != '\x00\n' and words[0] != '\x00Y\x00i\x00s\x00h\x00u\x00\n' :
        pass
    else:
        if words.__len__()==2:
            data= {
                'firstName': words[0],
                'middleName': '',
                'middleName': '',
                'middleName': '',
                'lastName': words[1],
                'fullName': words[0]+' '+words[1]
            }
            print(data['firstName'])
            json.dump(data, opf)
        elif words.__len__()==3:
            data= {
                'firstName': words[0],
                'middleName': words[1],
                'middleName': '',
                'middleName': '',
                'lastName': words[2],
                'fullName': words[0]+' '+words[1]+' '+words[2]
            }
            print(data['firstName'])
            json.dump(data, opf)
        elif words.__len__()==4:
            data= {
                'firstName': words[0],
                'middleName': words[1],
                'middleName': words[2],
                'middleName': '',
                'lastName': words[3],
                'fullName': words[0] + ' ' + words[1] + ' ' + words[2] +' ' + words[3]
            }
            print(data['firstName'])
            json.dump(data, opf)
        elif words.__len__()==5:
            data = {
                'firstName': words[0],
                'middleName': words[1],
                'middleName': words[2],
                'middleName': words[3],
                'lastName': words[4],
                'fullName': words[0] + ' ' + words[1] + ' ' + words[2] + ' ' + words[3]+' '+words[4]
            }
            print(data['firstName'])
            json.dump(data, opf)
opf.close()
temp.close()