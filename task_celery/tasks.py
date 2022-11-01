from celery import Celery
from celery.utils.log import get_task_logger
import time

# Celery Initiated
app = Celery("task_celery",
    broker='amqps://kponkjec:NOObx-xwGarzBp3GhYk4X4bOiQTPx_Z8@puffin.rmq2.cloudamqp.com/kponkjec',
    backend='rpc://'
)

logger = get_task_logger(__name__)

# Celery Task
@app.task(bind=True, name='task_celery.tasks.sum')
def sum(self, x, y):
    logger.info(f"task-{x} with args {x} + {y}")
    time.sleep(5)
    logger.info(f"task-{x} Finished")
    return x + y


