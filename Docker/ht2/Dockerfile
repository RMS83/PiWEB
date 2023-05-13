FROM python:latest

COPY ./requirements.txt /src/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src

WORKDIR src/stocks_products
EXPOSE 6060

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:6060"]
