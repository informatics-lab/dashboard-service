FROM python:3.6

RUN apt-get update

WORKDIR /usr/src/app
COPY ./weather_dashboards/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./weather_dashboards .

EXPOSE 8000

CMD gunicorn -b :8000 weather_dashboards.wsgi 
