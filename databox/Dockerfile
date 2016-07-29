from python:2.7

RUN pip install --upgrade google-api-python-client
RUN pip install oauth2
RUN pip install Flask
RUN pip install flask-restful
RUN pip install gntp

ADD . /code
WORKDIR /code

EXPOSE 5000

CMD ["python", "startup.py", "--noauth_local_webserver"]
 