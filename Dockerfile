FROM python:3.12-bookworm AS main

WORKDIR /work

RUN apt-get update && \
    apt-get install -y \
    snmp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN snmpget --version

ENTRYPOINT [ "python", "main.py" ]
