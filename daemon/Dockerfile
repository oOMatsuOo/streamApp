FROM python:latest

RUN apt-get update \
&& apt-get -y install cron \
&& pip3 install apscheduler \
&& pip3 install mariadb \
&& pip3 install tinytag \
&& pip3 install checksumdir \
&& apt-get update 

WORKDIR /usr/src/app

COPY python-cron /etc/cron.d/python-cron

RUN chmod 0644 /etc/cron.d/python-cron

RUN crontab /etc/cron.d/python-cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
