FROM ubuntu
ARG version
ENV VERSION=$version
RUN apt-get update && apt-get install -y \
	vim \
	python3 \
	zip \
	unzip \
	curl 

VOLUME /tmp
COPY src/zip_job.py /tmp
CMD ["/bin/bash", "-c", "echo FIRST COMMAND"]
//CMD ["/bin/bash", "-c lsb_release -a" ;"test -e /tmp/zip_job.py"]
