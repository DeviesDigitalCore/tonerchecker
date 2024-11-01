FROM python:3.12 AS main

WORKDIR /work

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN snmpget --version

ENTRYPOINT [ "python", "main.py" ]
