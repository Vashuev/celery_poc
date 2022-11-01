FROM python:3.10.2
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A task_celery.tasks worker -l info