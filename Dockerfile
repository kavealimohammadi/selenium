from centos:7
RUN pip3 install --upgrade pip

WORKDIR /app
COPY . /app

EXPOSE 4444

ENTRYPOINT ["python3"]
