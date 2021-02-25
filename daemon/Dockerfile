FROM python:latest

RUN apt-get update \
&& pip3 install apscheduler

WORKDIR /urs/src/app

CMD ["daemon.py"]
ENTRYPOINT [ "python3" ]