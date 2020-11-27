FROM python:3.8-buster as builder

RUN mkdir /code
WORKDIR /code

ADD entry.sh /code/entry.sh
ADD ../app /code
# ここからは実行用コンテナの準備
FROM python:3.8-slim-buster as runner

COPY requirements.lock /opt/app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN apt update \
  && apt install -y libpq5 libxml2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/code/"
ENV FLASK_APP "/code/proxy.py"
CMD ["/code/entry.sh"]