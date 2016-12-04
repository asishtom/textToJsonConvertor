import numpy as np
import json
import fileinput
import pandas as pd
table_cols=['first_name','middle_name_1','middle_name_2','middle_name_3','last_name','full_name']
x=input("File Name with path >")
data= pd.read_table(x, sep=' ', names=table_cols,skipinitialspace=True,skip_blank_lines=True)
#data.isnull().any(axis=1)
for index, d in data.iterrows():
    if d[1] is np.nan:
        d[5] = d[0]
    elif d[2] is np.nan :
        d[5] =d[0]+' '+d[1]
        d[4]= d[1]
        d[1]= np.nan
    elif d[3] is np.nan:
        d[5] = d[0] + ' ' + d[1]+' '+d[2]
        d[4]=d[2]
        d[2]= np.nan
    elif d[4] is np.nan:
        d[5] = d[0] + ' ' + d[1] + ' ' + d[2]+ ' ' + d[3]
        d[4] = d[3]
        d[3]= np.nan
    else:
        d[5] = d[0] + ' ' + d[1] + ' ' + d[2] + ' ' + d[3]+' '+d[4]

opf=open('C:/Users/asish/data.json', 'w')
#print(data)
json_str= data.to_json(orient='records')
parsed = json.loads(json_str)
opf.write(json.dumps(parsed, indent=4))
print (json.dumps(parsed, indent=4))
#C:/Users/asish/Andhra_Students.txt

opf.close()
