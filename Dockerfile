from python:3.9

ADD app.py .

ADD db.yaml .

RUN pip install mysql-connector-python pyyaml

CMD ["python", "./app.py"]