FROM python:3.11.4

WORKDIR /app

COPY ./src/ /app

RUN apt-get update && \
    apt-get install -y python3-venv python3-dev python3-pip

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/python -m pip install --upgrade pip

RUN /opt/venv/bin/python -m pip install -r requirements.txt

CMD ["/opt/venv/bin/python", "-m", "http.server", "8080"]
