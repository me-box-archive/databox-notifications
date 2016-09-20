from python:2.7

RUN apt-get update && apt-get install -y libsodium13 libsodium-dev

ADD . /code

WORKDIR /code
RUN curl -O mysql-connector.deb http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python_2.1.3-1ubuntu15.04_all.deb
RUN dpkg -i mysql-connector.deb

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "startup.py", "--noauth_local_webserver"]
