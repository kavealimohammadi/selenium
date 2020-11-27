from centos:7
RUN pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
