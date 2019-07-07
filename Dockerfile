FROM python:3.7.3-alpine3.9

# Unbuffer the entire app (flush immediately) to enable docker logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ADD *.py requirements.txt ./
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]