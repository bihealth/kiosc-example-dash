FROM python:3.8-buster

MAINTAINER Oliver Stolpe <oliver.stolpe@bih-charite.de>
LABEL org.opencontainers.image.source https://github.com/bihealth/kiosc-example-dash

ARG app_git_url=https://github.com/bihealth/kiosc-example-dash.git
ARG app_git_tag
ARG app_git_depth=1

ENV DEBIAN_FRONTEND noninteractive

# Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /usr/local/bin/wait
RUN chmod +x /usr/local/bin/wait

# Copy source code into Docker image.
RUN mkdir -p /usr/src
RUN git clone --depth $app_git_depth --branch $app_git_tag $app_git_url /usr/src/app

# Install Python dependencies.
RUN cd /usr/src/app && \
    pip install -r requirements.txt

# Define the entry point.
COPY docker-entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && \
    ln -s /usr/local/bin/docker-entrypoint.sh / # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 8050/tcp
