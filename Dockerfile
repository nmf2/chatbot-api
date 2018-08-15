FROM nmf2/eva:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

RUN python3 setup.py install

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "chatbot_server"]