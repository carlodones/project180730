# -*- coding: utf-8 -*-
import json
import time
import datetime
import random

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data

mainData={
            'timestampDevice': 0000000000000,
            'qos': "Gqos",
            'values': [
             ]
        }

splitData={
            'payload': 9999,
            'address': 'ADDR',
            'qos': 'Sqos',
            'timestampDevice': 0000000000000
        }
'''
d = {"name":"interpolator",
"children":[{'name':key,"size":value} for key,value in sample.items()]}
j = json.dumps(d, indent=4)
f = open('sample.json', 'w')
print >> f, j
f.close()
'''
#sample = {235.5:'TEMP01':'GOOD':time.ctime(time.time()), 235.5:'TEMP02':'GOOD':time.ctime(time.time()), 235.5:'FLOW01':'GOOD':time.ctime(time.time())}

'''
sample = {
            'payload': 9999,
            'address': 'ADDR',
            'qos': 'Sqos',
            'timestampDevice': 0000000000000
        }

keys = ["payload", "address", "qos", "timestampDevice"]
values = [random.uniform( 0, 100 ), "TEMP01", "GOOD", time.time()]
for i in keys:
        dicts[i] = values[i]
print(dicts)
'''
sample = {235.5: 'TEMP01',  240.5: 'TEMP02', 180: 'PRESS01'}
#sample=[(235.5, 'TEMP01', 'A'), (240.5, 'TEMP02', 'B'), (180, 'PRESS01', 'C')]
'''
sample = [{
            '1': 235.5,
            '2': 'TEMP01',
            '3': 'A',
            '4': 'A'
            },
            {
            '1': 240.5,
            '2': 'TEMP02',
            '3': 'B',
            '4': 'B'
            }
            ]
'''

value3=123
value4=time.time()

mainData = {'timestampDevice': value4,'qos': "GOOD",'values': [{'payload':value1,"address":value2,"qos":value3,"timestampDevice":value4} for value1,value2 in sample.items()]}
#mainData = {'timestampDevice': value4,'qos': "GOOD",'values': [{'payload':value[0],"address":value[1],"qos":value[2],"timestampDevice":value[0]} for value in sample.items()]}
#splitData = json.dumps(mainData)

#splitData=json.dumps({'payload': pL,'address': pADDR,'qos': pQOS,'timestampDevice': pTIMESTAMP} for pL,pADDR,pQOS,pTIMESTAMO in sample.items(), indent=4)

# Write JSON file
with io.open('./cfg/dataTest.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(mainData,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

'''
{
   'timestampDevice': 0000000000000, // <- Default value
   'qos': "Gqos", // <- Default value
   'values': [
      {
         'payload': 9999, // <- This MUST be a Number
         'address': 'ADDR', // <- Mandatory
         'qos': 'Sqos' // <- Optional, overrides default
         'timestampDevice': 0000000000000 // <- Optional, overrides default
      }
   ]
}
'''

'''
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}
'''

'''
for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
'''





'''
# Write JSON file
with io.open('./cfg/dataTest.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('./cfg/dataTest.json') as data_file:
    data_loaded = json.load(data_file)

print data_loaded
print(data == data_loaded)
'''