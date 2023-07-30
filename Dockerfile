FROM python:3.10-buster

RUN apt-get -y update && apt-get install -y build-essential cmake

ADD facial_extraction ./facial_extraction

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /facial_extraction/interface

CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
