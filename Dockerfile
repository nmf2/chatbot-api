FROM nmf2/eva:latest

RUN mkdir -p /tmp

# mv nltk data to eva's
RUN mkdir /elasticsearch /root/.bot/

COPY requirements.txt /tmp

RUN cd /tmp \
    && pip3 install --no-cache-dir -r requirements.txt

COPY . /tmp/

RUN cd /tmp \
    && python3 setup.py install

RUN rm -rf /tmp

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "chatbot_server"]