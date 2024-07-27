FROM python:3.12.4-bullseye
WORKDIR /app
RUN apt-get update && apt-get install -y
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
