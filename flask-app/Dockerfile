FROM python:3.9-alpine
WORKDIR /app
COPY ./app.py /app
RUN pip install flask psycopg2-binary
CMD ["python", "app.py"]
