FROM thatsrashmi/python.3.9.16-alpine3.18-base
LABEL authors="kjgue"
LABEL maintainer="kjgueye@hotmail.com"



RUN pip install flask
RUN pip install xmltodict

WORKDIR /home/karim/CiscoDev/globalmantics_crm


EXPOSE 5000/tcp

ENTRYPOINT ["python"]
CMD ["start.py"]
