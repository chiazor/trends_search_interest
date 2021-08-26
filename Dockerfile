FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev



WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["python3", "./app.py"]



