from python:2.7

RUN apt-get update && apt-get install -y libsodium13 libsodium-dev

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "startup.py", "--noauth_local_webserver"]
