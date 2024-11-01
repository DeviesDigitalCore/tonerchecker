FROM python:3.12 AS main

WORKDIR /work

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]
