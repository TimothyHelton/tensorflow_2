FROM nvcr.io/nvidia/tensorflow:20.09-tf2-py3

WORKDIR /usr/src/tensorflow_2

COPY . .

RUN cd /opt \
	&& apt-get update -y \
	#&& apt-get upgrade -y \  Do not upgrade NVIDIA image OS
	&& apt-get install -y \
		apt-utils \
		protobuf-compiler \
	&& git clone \
		--branch master \
		--single-branch \
		--depth 1 \
		https://github.com/tensorflow/models.git \
	&& cd /opt/models/research \
	&& protoc object_detection/protos/*.proto --python_out=. \
	&& cd /usr/src/tensorflow_2 \
	&& pip install --upgrade pip \
	&& pip install -e .[all] \
	&& rm -rf /tmp/* \
	&& rm -rf /var/lib/apt/lists/* \
	&& apt-get clean

ENV PYTHONPATH $PYTHONPATH:/opt/models/research:/opt/models/research/slim:/opt/models/research/object_detection

CMD [ "/bin/bash" ]
