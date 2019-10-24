FROM debian:buster-slim

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && \
    apt-get -yq dist-upgrade && \
    apt-get -yq --no-install-recommends install python3-selenium chromium-driver && \
    apt-get clean && \
    apt-get -yq autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get -yq --no-install-recommends install python3-yaml python3-distutils chromium-sandbox && \
    apt-get clean && \
    apt-get -yq autoremove && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m -u 10000 --skel /etc/skel -s /bin/bash duration


COPY duration.py /app

USER duration
CMD ["/app"]
