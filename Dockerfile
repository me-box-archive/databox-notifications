from python:2.7

RUN apt-get update && apt-get install -y libsodium13 libsodium-dev

ADD ./databox /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "startup.py", "--noauth_local_webserver"]