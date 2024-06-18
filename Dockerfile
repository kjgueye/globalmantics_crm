FROM thatsrashmi/python.3.9.16-alpine3.18-base
LABEL authors="kjgue"
LABEL maintainer="kjgueye@hotmail.com"



RUN pip install flask
RUN pip install xmltodict

RUN mkdir -p /app


COPY . /app


WORKDIR /app


RUN ls -la /app

EXPOSE 5000/tcp

ENTRYPOINT ["python", "start.py"]

