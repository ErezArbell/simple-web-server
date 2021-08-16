FROM python:3.9-alpine

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py /opt/
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port 8080
