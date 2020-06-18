FROM registry.access.redhat.com/rhscl/python-36-rhel7 as base

COPY docker/requirements.txt /app/
COPY src/app.py /app/

ARG BUILD_NUMBER_ARG

WORKDIR /app

RUN pip install --index=http://repos.techpark.local/repository/pypi-proxy/simple --trusted-host repos.techpark.local -r requirements.txt

USER root
RUN sed -i "s/<build_number>/$BUILD_NUMBER_ARG/g" ./app.py
RUN mkdir -p /app/logs

ENTRYPOINT ["python"]
CMD ["app.py"]
