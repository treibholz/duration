FROM alpine

RUN apk add --no-cache chromium chromium-chromedriver py3-yaml python3

RUN pip3 install selenium && \
    rm -rf ~/.cache

RUN adduser -u 10000 -D duration
COPY duration.py /app

USER duration
CMD ["/app"]
