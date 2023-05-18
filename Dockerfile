FROM python:3.10-alpine
RUN apk add --no-cache gcc musl-dev linux-headers

COPY . /code
WORKDIR /code

RUN pip install --upgrade setuptools
RUN pip install -r /code/requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000
ENTRYPOINT ["/code/docker-entrypoint.sh"]