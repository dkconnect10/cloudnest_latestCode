FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# Use environment variable DJANGO_SETTINGS_MODULE
CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000"]
