FROM python:latest

RUN apt-get update \
&& pip3 install requests \
&& pip3 install mariadb \
&& pip3 install moviepy \
&& pip3 install tinytag \
&& pip3 install checksumdir \
&& apt-get update

WORKDIR /usr/src/app

CMD ["test.py"]
ENTRYPOINT ["python3"]