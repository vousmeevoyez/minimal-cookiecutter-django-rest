FROM python:3.7 AS base
MAINTAINER KELVIN
ARG dependencies=requirements
ENV dependencies=${dependencies}
COPY ./requirements /requirements
RUN pip install -r /requirements/${dependencies}.txt
WORKDIR /app
COPY . /app

# second stage build
FROM python:3.7-slim AS release
RUN apt-get update && apt-get install make
WORKDIR /app
ARG dependencies=requirements
ENV dependencies=${dependencies}
COPY --from=base /app/requirements/${dependencies}.txt ./
COPY --from=base /root/.cache /root/.cache
RUN pip install -r ${dependencies}.txt
# copy again
COPY --from=base /app ./
