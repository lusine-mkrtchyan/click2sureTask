FROM python:3.5

# add requirements.txt to the image
ADD task/requirements.txt /app/requirements.txt
ADD ./task/ /app/
# set working directory to /app/
WORKDIR /app

# install python dependencies
RUN pip install -r requirements.txt
