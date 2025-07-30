FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install flask

ENV AUTHOR="Default Author"
EXPOSE 8000

CMD ["python", "app.py"]
