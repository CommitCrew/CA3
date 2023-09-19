From python 
ENV USERNAME = hadiya
RUN mkdir -p D:\University\Semester 7\MLOPs\docker_demo
COPY . D:\University\MLOPs\Semester 7\Docker
EXPOSE 5000
WORKDIR D:\University\MLOPs\Semester 7\Docker
RUN pip install -r requirements.txt
CMD ['python','test_main.py']

#docker build -t docker_demo:1.0 .  
#ls
#docker images
#docker run docker_demo:1.0  
#docker run -it docker_demo:1.0  
#docker run docker_demo:1.0  sleep infinity
#docker exec -it (id of container here) /bin/bash
#build again after changing the docker file