import random
import time
from celery import Celery

time.sleep(20)

print('Application started')

app = Celery(
    'celery_poc',
    broker='amqp://admin:mypass@rabbit:5672',
    # broker = 'amqps://kponkjec:C5UBm8LH6_hm1rP9aelB4oBzewjT1OXm@puffin.rmq2.cloudamqp.com/kponkjec',
    backend='rpc://admin:mypass@rabbit:5672'
    # backend = 'rpc://kponkjec:C5UBm8LH6_hm1rP9aelB4oBzewjT1OXm@puffin.rmq2.cloudamqp.com/kponkjec',
)

numTasks = 5
tasks = []

for i in range(numTasks):
    time.sleep(2 * random.random())  #delay
    tasks.append(
        app.send_task('addTask', (i, 3))  # Send task by name
    )
    print('Sent task:', i)

for task in tasks:
    result = task.get()
    print('Received result:', result)

print('Application ended')