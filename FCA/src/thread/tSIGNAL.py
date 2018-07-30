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



sample = {235.5: 'TEMP01',  240.5: 'TEMP02', 180: 'PRESS01'}


value3=123
value4=time.time()

mainData = {'timestampDevice': value4,'qos': "GOOD",'values': [{'payload':value1,"address":value2,"qos":value3,"timestampDevice":value4} for value1,value2 in sample.items()]}

# Write JSON file
with io.open('/usr/src/app/src/MQTT/message.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(mainData,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))






