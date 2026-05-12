import time
from datetime import datetime

def task():
    with open('time_log.txt','a') as f:
        f.write(f"script ran at: {datetime.now()}\n")
    print(f'task ran at : {datetime.now()}\n')

while True:
    task()
    time.sleep(10)