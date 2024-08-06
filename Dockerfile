FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /agromap/backend

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./requirements-dev.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements-dev.txt

COPY . .

RUN chmod +x backend.entrypoint.sh

ENTRYPOINT [ "sh","./backend.entrypoint.sh" ]
