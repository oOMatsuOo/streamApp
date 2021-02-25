FROM python:latest

RUN apt-get update \
&& pip3 install apscheduler \
&& pip3 install mariadb \
&& pip3 install tinytag \
&& pip3 install checksumdir \
&& apt-get update

WORKDIR /usr/src/app

CMD ["daemon.py"]
ENTRYPOINT [ "python3" ]