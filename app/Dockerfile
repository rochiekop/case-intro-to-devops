FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install --upgrade 'sentry-sdk[flask]'

EXPOSE 5000

CMD ["python", "app.py"]