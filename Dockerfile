# My Dockerfile

# Image - Base Image
FROM debian:latest as base

## Update
RUN apt-get update -y

# Image - essentials Image
FROM base as essentials

## Install essential packages
RUN \
    apt-get install -y --no-install-recommends \
    git \
    zsh \
    curl \
    vim \
    wget \
    python \
    pip \
    nano

# Image - tools Image
FROM essentials as angelsetup
RUN \
    pip3 install smartapi-python \
    pip install websocket-client

###Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

### Angel Code here
RUN mkdir angel && cd angel
RUN wget https://github.com/ThetaGainer/dockerangel/blob/main/corecode.py

## Last command
ENTRYPOINT /bin/zsh
