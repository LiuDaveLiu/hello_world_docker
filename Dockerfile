# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM python:latest

# set working directory
WORKDIR /app

# install pip
RUN apt-get update && apt-get install -y python3-pip

# update pip
RUN pip3 install --upgrade pip

# add requirements
COPY ./requirements.txt /app/requirements.txt

# install requirements
RUN pip3 install -r requirements.txt

CMD python main.py

COPY src/*.* .
# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.
#COPY main.py /

# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
#CMD [ "python", "main.py" ]
