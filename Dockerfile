FROM python:3.13 AS main

WORKDIR /work

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]
