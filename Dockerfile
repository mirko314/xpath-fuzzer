FROM openjdk:latest
RUN apt-get update
# Install XPATH Libs
RUN apt-get install python3 python3-pip --assume-yes
RUN apt-get install libxml2
RUN apt-get install basex --assume-yes
RUN apt-get install xqilla --assume-yes
RUN apt-get install gcc make vim --assume-yes
RUN apt-get install python3-lxml=3.7.1-1 --assume-yes
# Ruby
#sudo apt install software-properties-common
#sudo apt-add-repository ppa:brightbox/ruby-ng -y
#sudo apt-get update
#\curl -sSL https://get.rvm.io | bash -s stable --ruby
RUN apt-get update
RUN apt-get install build-essential patch ruby-dev zlib1g-dev liblzma-dev bundler --assume-yes --fix-missing
RUN gem install nokogiri:1.10.1 rexml:3.2.1


# For Development comment out the next two lines and instead of Copy bind the Repo as Volume
# Then start the docker container and execute make manually
COPY . /app
RUN cd /app/libraries && bash ./compile.sh

# xmllib2 script currently not really usable
# RUN cd /app/libraries/xmllib2 && make


# Install Antlr4, later maybe used for automatic xpath generation based on xpath grammar
RUN cd /usr/local/lib && wget https://www.antlr.org/download/antlr-4.7.2-complete.jar
RUN echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.7.2-complete.jar"' >> ~/.bashrc && echo 'alias grun="java org.antlr.v4.gui.TestRig"' >> ~/.bashrc && echo 'export CLASSPATH=".:/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH"' >> ~/.bashrc
# RUN cd /app/antlr4 && antlr4 xpath.g4 && javac xpath*.java
RUN pip3 install grammarinator
# grun xpath main -tree
WORKDIR "/app"
