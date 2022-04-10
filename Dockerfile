FROM ubuntu:latest

RUN set -xe \
    && apt-get update -y \
    && apt-get install python3-pip -y

RUN pip3 install --upgrade pip
RUN pip3 install -U setuptools

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
