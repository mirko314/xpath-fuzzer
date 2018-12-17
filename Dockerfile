FROM gcc:latest
RUN apt-get update
# Install XPATH Libs
RUN apt-get install libxml2
RUN apt-get install basex --assume-yes
RUN apt-get install xqilla --assume-yes
COPY . /home

WORKDIR "/home"
