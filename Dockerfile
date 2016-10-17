from python:2.7

RUN apt-get update && apt-get install -y libsodium13 libsodium-dev

ADD ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

LABEL databox.type="notifications"

EXPOSE 8080

CMD ["python", "startup.py", "--noauth_local_webserver"]
