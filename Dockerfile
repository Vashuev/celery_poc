FROM python:3.10.2
ADD requirements.txt ./
RUN pip install -r requirements.txt

COPY . /
WORKDIR /