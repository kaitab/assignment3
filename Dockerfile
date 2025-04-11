FROM python:3.12

#create directory, I just used the one in the slides
WORKDIR /app

#copy everything here
COPY . .

#install our requirements
RUN pip install --no-cache-dir -r requirements.txt

#set a port number, no idea what this is, found it in the tutorial
EXPOSE 5000

CMD ["python", "./run.py"]

