# Ubuntu 18.04 with Java 8 installed.
# Build image with:  docker build -t arun/webserviceapi:v1 .

FROM ubuntu:18.04
MAINTAINER Arun Mohan K

RUN apt-get update

CMD echo ” Updating/Installing Python 3”
RUN apt-get install --yes python3.8

CMD echo ” Updating/Installing Python 3 PIP,flask,boto3”
RUN apt-get install --yes python3-pip && \
        pip3 install flask && \
        pip3 install boto3  && \
        apt-get upgrade -y

RUN pip3 install awscli

ARG AWS_KEY='AKIAXJIV5XUGFVFNAD4Z'
ARG AWS_SECRET_KEY='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'
ARG AWS_REGION='us-east-2'

RUN aws configure set aws_access_key_id $AWS_KEY
RUN aws configure set aws_secret_access_key $AWS_SECRET_KEY
RUN aws configure set default.region $AWS_REGION


RUN apt-get update

ENV REGION us-east-2
RUN export REGION
ENV END_URL https://dynamodb.us-east-2.amazonaws.com:8000
RUN export END_URL

EXPOSE 5000

RUN mkdir -p /home/poc/webservice/
COPY ./app/ /home/poc/webservice/
WORKDIR /home/poc/webservice
CMD python3 loan_wbservice.py
