FROM java:7

ADD /jflex-1.6.1 /jflex-1.6.1

ENV PATH "$PATH:/jflex-1.6.1/bin"

WORKDIR "/compiladores"
