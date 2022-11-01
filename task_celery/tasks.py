from celery import Celery
from celery.utils.log import get_task_logger
import time

# Celery Initiated
app = Celery("task_celery",
    broker='amqp://admin:mypass@rabbit:5672',
    # broker = 'amqps://kponkjec:C5UBm8LH6_hm1rP9aelB4oBzewjT1OXm@puffin.rmq2.cloudamqp.com/kponkjec',
    backend='rpc://'
)

logger = get_task_logger(__name__)

# Celery Task
@app.task(name="task_celery.tasks.sum")
def sum(x, y):
    logger.info(f"task-{x} with args {x} + {y}")
    time.sleep(5)
    logger.info(f"task-{x} Finished")
    return x + y


