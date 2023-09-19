
FROM python:3.10
ENV USERNAME = commitcrew
RUN mkdir -p /home/dockerdemo
COPY . /home/dockerdemo
EXPOSE 5000
WORKDIR /home/dockerdemo
RUN pip install -r requirements.txt
RUN pip install flask
CMD ['python','test.py']

