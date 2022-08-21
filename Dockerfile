#set base image (host OS)
FROM python:3.6.5

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --proxy http://proxy.kavosh.org:808 --upgrade pip
RUN pip install --proxy http://proxy.kavosh.org:808 -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
CMD [ "python", "./usage-api.py" ]
