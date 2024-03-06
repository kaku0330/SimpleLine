FROM python:3.11.6

WORKDIR /app

COPY . /app

EXPOSE 8000

# Install needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR testDrf

# CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
CMD ["python3","-m","uvicorn","testDrf.asgi:application","--host","0.0.0.0","--port","8000","--reload","--workers","2"]
