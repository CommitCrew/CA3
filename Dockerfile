FROM python:3.10
ENV USERNAME=zuhaumar
RUN mkdir -p /home/dockerdemo
COPY . /home/dockerdemo
EXPOSE 5000
WORKDIR /home/dockerdemo
RUN pip install -r requirements.txt
CMD ["python3","test.py"]