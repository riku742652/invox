FROM python:3.12.4-bullseye
WORKDIR /mock
RUN apt-get update && apt-get install -y
COPY . /mock
RUN pip install -r requirements.txt
CMD ["python", "mock_app.py"]
