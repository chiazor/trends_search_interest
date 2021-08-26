FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev



WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000



CMD ["python", "./app.py"]

