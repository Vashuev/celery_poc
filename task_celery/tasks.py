from celery import Celery
from celery.utils.log import get_task_logger
import time

# Celery Initiated
app = Celery("task_celery",
    broker='amqp://admin:mypass@rabbit:5672',
    backend='rpc://',
    include=["task_celery.tasks"]
)

logger = get_task_logger(__name__)

# Celery Task
@app.task
def sum(x, y):
    logger.info(f"task-{x} with args {x} + {y}")
    time.sleep(5)
    logger.info(f"task-{x} Finished")
    return x + y


