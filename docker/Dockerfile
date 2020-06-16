ARG RH_REGISTRY_ARG
FROM registry.access.redhat.com/rhscl/python-36-rhel7 as base

COPY docker/requirements.txt /app/
COPY src/app.py /app/

ARG BUILD_NUMBER_ARG
ARG PYPI_BASE_URL_ARG
ARG PYPI_PATH_URL_ARG
ARG PYPI_TRUSTED_HOST_ARG

WORKDIR /app

RUN pip install -r requirements.txt

USER root
RUN sed -i "s/<build_number>/$BUILD_NUMBER_ARG/g" ./app.py
RUN mkdir -p /app/logs

ENTRYPOINT ["python"]
CMD ["app.py"]
