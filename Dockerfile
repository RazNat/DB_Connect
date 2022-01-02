#from python:3.9

#ADD app.py .

#ADD db.yaml .

#RUN pip install mysql-connector-python pyyaml pandas

#CMD ["python", "./app.py"]

# Python image to use.
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install pandas numpy mysql-connector-python pyyaml

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
ENTRYPOINT ["python", "app.py"]