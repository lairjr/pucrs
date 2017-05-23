FROM java:latest

RUN apt-get update
RUN apt-get install -y jflex byacc-j
RUN apt-get install -y make
