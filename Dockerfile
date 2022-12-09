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
CMD ["lsb_release", "-a"]
CMD ["test", "-e", "/tmp/zip_job.py"]
