FROM python:3.11.6

WORKDIR /app

COPY . /app

EXPOSE 8000

# Install needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

CMD /app
