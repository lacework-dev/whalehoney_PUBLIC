FROM ubuntu:20.04
RUN mkdir /opt/app && useradd -u 2000 ubuntu
WORKDIR /opt/app
COPY dockerapi/ /opt/app/dockerapi
COPY wsgi.py /opt/app/
COPY requirements.txt /opt/app/
RUN apt-get update -y && \
    apt-get install python3 python3-pip gunicorn -y && \
    pip3 install -r requirements.txt && chown 2000:2000 -R /opt/app;
USER ubuntu
ENTRYPOINT ["/usr/bin/gunicorn", "wsgi:app", "-b", "0.0.0.0:2375"]
