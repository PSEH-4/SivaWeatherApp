FROM python:2.7-slim

WORKDIR /src

COPY ./src /src

EXPOSE 5000

RUN pip install -r requirements.txt  && rm requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]