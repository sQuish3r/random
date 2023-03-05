FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code

CMD ["uvicorn", "web_app:app", "--host", "0.0.0.0", "--port", "8088"]