FROM centos:centos7
WORKDIR /code
# Install Python
RUN yum update -y
RUN yum install -y python3
RUN yum install python3-pip -y
# PostgreSQL dependencies
RUN yum install postgresql -y 
RUN yum install postgresql-devel -y 
RUN yum install python3-devel -y
RUN yum -y install gcc
# Install python modules needed
COPY ./pythonModules.txt ./pythonModules.txt
RUN pip3 install --no-cache-dir --upgrade -r pythonModules.txt
# Copy scripts & data
COPY ./DB.py ./
COPY ./main.py ./
COPY ./Sample.csv ./
COPY ./ingestData.sh ./
COPY ./initCentosAPI.sh ./
COPY ./validateFields.py ./
# SET UTF-8 and run API
ENV LC_CTYPE=en_US.UTF-8 
CMD [ "bash", "initCentosAPI.sh" ]