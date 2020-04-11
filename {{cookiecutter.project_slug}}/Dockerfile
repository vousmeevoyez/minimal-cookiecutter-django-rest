FROM python:3.7 AS base
COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app

FROM python:3.7-slim AS release
RUN apt-get update && apt-get install make
WORKDIR /app
COPY --from=base /app/requirements.txt ./
COPY --from=base /root/.cache /root/.cache
RUN pip install -r requirements.txt
COPY --from=base /app ./
