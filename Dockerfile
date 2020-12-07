FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3.8 -y
RUN apt install python3-pip -y

COPY . .

RUN /bin/bash -c "source venv/bin/activate"
RUN pip3 install -r pixelstarmusic/requirements.txt

EXPOSE 8113

CMD source venv/bin/activate
CMD python3 ./pixelstarmusic/manage.py runserver 0.0.0.0:8113

#sudo docker build -t pixel .

#sudo docker run --name pixel-api -t -p 8113:8113 -d pixel