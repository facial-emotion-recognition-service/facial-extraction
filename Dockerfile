FROM python:3.10-buster

WORKDIR /facial_extraction

RUN apt-get -y update && apt-get install -y build-essential cmake

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY facial_extraction .

EXPOSE 8000

WORKDIR /facial_extraction/interface
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
