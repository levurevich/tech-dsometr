FROM registry.access.redhat.com/rhscl/python-36-rhel7:latest

COPY /src/app.py /app

ARG BUILD_NUMBER_ARG

WORKDIR /app

RUN pip install -r requirements.txt

USER root
RUN sed -i "s/<build_number>/$BUILD_NUMBER_ARG/g" ./app.py

ENTRYPOINT ["python"]
CMD ["app.py"]