FROM python:3.10.2
ADD requirements.txt /app/requirements.txt
ADD ./task_celery/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A task_celery.tasks worker --loglevel=info
#ENTRYPOINT ['celery','-A','task_celery.tasks', 'worker', '--loglevel=info']