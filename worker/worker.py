import random
from turtle import back
from celery import Celery
from celery.utils.log import get_task_logger
import time

time.sleep(10)

print('Worker started')

app = Celery(
    'celery_poc',
    broker='amqp://admin:mypass@rabbit:5672',
    # broker = 'amqps://kponkjec:C5UBm8LH6_hm1rP9aelB4oBzewjT1OXm@puffin.rmq2.cloudamqp.com/kponkjec',
    backend='rpc://admin:mypass@rabbit:5672'
    # backend = 'rpc://kponkjec:C5UBm8LH6_hm1rP9aelB4oBzewjT1OXm@puffin.rmq2.cloudamqp.com/kponkjec',
)
logger = get_task_logger(__name__)

# Celery Task
@app.task(name="addTask")
def sum(x, y):
    logger.info(f"task-{x} with args {x} + {y}")
    time.sleep(10*random.random())
    logger.info(f"task-{x} Finished")
    return x + y


