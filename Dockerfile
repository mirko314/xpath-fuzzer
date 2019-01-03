FROM openjdk:latest
RUN apt-get update
# Install XPATH Libs
RUN apt-get install libxml2
RUN apt-get install basex --assume-yes
RUN apt-get install xqilla --assume-yes
RUN apt-get install make --assume-yes
RUN apt-get install gcc --assume-yes
RUN apt-get install vim --assume-yes

# For Development comment out the next two lines and instead of Copy bind the Repo as Volume
# Then start the docker container and execute make manually
COPY . /app
# RUN cd /app/libraries/xmllib2 && make

RUN cd /usr/local/lib && wget https://www.antlr.org/download/antlr-4.7.2-complete.jar
RUN echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.7.2-complete.jar"' >> ~/.bashrc && echo 'alias grun="java org.antlr.v4.gui.TestRig"' >> ~/.bashrc && echo 'export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"' >> ~/.bashrc

# RUN cd /app/antlr4 && antlr4 xpath.g4 && javac xpath*.java
#grun xpath main -tree

WORKDIR "/app"
