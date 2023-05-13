FROM debian:bullseye

WORKDIR /src
# copie de requirements.txt pour installer les modules
ADD requirements.txt /src
ENV PYTHONUNBUFFERED=1 
# installer python, pip, nginx et les modules
# RUN  apt-get install python3  &&  apt install python3-pip  &&  apt install nginx  && pip install -r requirements.txt
RUN  apt-get update 
RUN  apt-get install python3 python3-pip python3-dev curl -y

RUN pip3 install -r requirements.txt


# copie du projet 
ADD . /src/

RUN python3 manage.py makemigrations && python3 manage.py migrate