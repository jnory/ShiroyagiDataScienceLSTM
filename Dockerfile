FROM nvidia/cuda:7.5-cudnn5-devel-ubuntu14.04

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64
ENV CUDA_HOME /usr/local/cuda

RUN apt-get update && apt-get install -y wget git \
    && cd /tmp \
    && wget https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh \
    && chmod 755 ./Anaconda3-4.1.1-Linux-x86_64.sh \
    && ./Anaconda3-4.1.1-Linux-x86_64.sh -b -p /opt/anaconda \
    && /opt/anaconda/bin/pip install keras \
    && mkdir /root/.keras \
    && mkdir /etc/cert \
    && openssl req -x509 -nodes -days 365 -newkey rsa:2048 -sha256 -keyout /etc/cert/jupyter.key -out /etc/cert/jupyter.pem -batch

ADD keras.json /root/.keras/keras.json
ADD dot.theanorc /root/.theanorc

ENV PATH $PATH:/opt/anaconda/bin