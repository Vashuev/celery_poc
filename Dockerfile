FROM python:3.10.2
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD ./task_celery/ /app/task_celery/
WORKDIR /