FROM python:3.10

WORKDIR /app

COPY ../backend/requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ../backend /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
