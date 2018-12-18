FROM gcc:latest
RUN apt-get update
# Install XPATH Libs
RUN apt-get install libxml2
RUN apt-get install basex --assume-yes
RUN apt-get install xqilla --assume-yes

# For Development comment out the next two lines and instead of Copy bind the Repo as Volume
# Then start the docker container and execute make manually
COPY . /app
RUN cd /app/libraries/xmllib2 && make

WORKDIR "/app"
