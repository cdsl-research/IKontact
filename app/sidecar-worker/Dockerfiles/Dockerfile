FROM python:3.7

RUN mkdir /code
WORKDIR /code

ADD entry.sh /code/entry.sh
ADD ../app /code

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000
ENV PYTHONPATH "${PYTHONPATH}:/code/"
ENV FLASK_APP "/code/proxy.py"
CMD ["/code/entry.sh"]