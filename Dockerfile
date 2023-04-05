FROM python:3.10.4
FROM nginx:1.23.4

WORKDIR /app

COPY app.py ./
COPY infodb.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN wget -O backend.zip https://www.dropbox.com/s/apyoabvieotk13s/backend.zip?dl=1
RUN apt install unzip -y
RUN unzip backend.zip
RUN rm backend.zip

CMD [ "python", "app.py" ]


