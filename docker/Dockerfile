
FROM python:3 as base

COPY docker/requirements.txt /app/
COPY src/app.py /app/

ARG BUILD_NUMBER_ARG
ARG PYPI_BASE_URL_ARG
ARG PYPI_PATH_URL_ARG
ARG PYPI_TRUSTED_HOST_ARG

WORKDIR /app

RUN pip install -r requirements.txt

USER root
RUN sed  -i "s/<build_number>/qweqweqwe/g" ./app.py
RUN mkdir -p /app/logs
RUN chmod 777 /app/logs

ENTRYPOINT ["python"]
CMD ["app.py"]