#!/usr/bin/env python3
import asyncio  
import time  
from datetime import datetime
from threading import Thread

async def function(name, number, wait):
    while True:
        pass
        start = time.time()  

        await asyncio.sleep(wait)

        try:
            print('check command ',name)
            filePointer = open('./FCA/src/thread/alt.sto', 'r')
            #filePointer = open('/usr/src/app/src/thread/alt.sto', 'r')
                          
            try:
                print('command ALT ',name)
                filePointer.close
                break
            finally:
                filePointer.close
        except IOError as e:
            print('loop')

        end = time.time()  
        print("Total time: {}".format(end - start))

loop = asyncio.get_event_loop()
start = time.time()  
tasks = [  
    asyncio.ensure_future(function("A", 3, 3)),
    asyncio.ensure_future(function("B", 10, 2)),
]
loop.run_until_complete(asyncio.wait(tasks))  

end = time.time()  
print("Total time: {}".format(end - start))  