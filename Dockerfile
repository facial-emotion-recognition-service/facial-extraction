FROM python:3.10-buster

RUN apt-get -y update && apt-get install -y build-essential cmake

ADD facial_extraction ./facial_extraction

COPY requirements.txt .
COPY setup.py .

RUN pip install --upgrade pip
RUN pip install .

# This section only applies when running the container in standalone mode.
# When docker-compose is used, the `environment` section of docker-compose.yml
# automatically takes precendence over the `ENV` commands below.
WORKDIR /facial_extraction
RUN mkdir input_images
ENV IMAGE_INPUT_DIR="../input_images/"

EXPOSE 8000
WORKDIR /facial_extraction/interface
CMD ["python", "main_server.py", "runserver", "0.0.0.0:8000"]
