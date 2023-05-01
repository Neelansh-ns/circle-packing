FROM python:3.9-slim-buster

# set the working directory in the container
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt .

# install the dependencies
RUN pip install -r requirements.txt

# copy the rest of the application code into the container
COPY . .

# expose the port on which the application will run
EXPOSE 5001

# start the application
CMD [ "python", "app.py" ]
