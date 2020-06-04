ARG RH_REGISTRY_ARG
FROM ${RH_REGISTRY_ARG}/rhscl/python-36-rhel7 as base

COPY docker/requirements.txt /app/
COPY src/app.py /app/

ARG BUILD_NUMBER_ARG
ARG PYPI_BASE_URL_ARG
ARG PYPI_PATH_URL_ARG
ARG PYPI_TRUSTED_HOST_ARG

WORKDIR /app

RUN pip install --index=http://${PYPI_BASE_URL_ARG}${PYPI_PATH_URL_ARG} --trusted-host ${PYPI_TRUSTED_HOST_ARG} -r requirements.txt

USER root
RUN sed -i "s/<build_number>/$BUILD_NUMBER_ARG/g" ./app.py

ENTRYPOINT ["python"]
CMD ["app.py"]