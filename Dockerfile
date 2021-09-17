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
    pip install pandas \
    pip install websocket-client    

###Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

### Telegram
RUN mkdir -p /root/echo-bot/
WORKDIR cd echo-bot/

RUN \
    pip install --user pipenv \
    python3 -m pipenv pipenv install python-telegram-bot \
    wget https://raw.githubusercontent.com/ThetaGainer/Telegram/main/bot.py
    
# Telegram Run Server
# python3 -m pipenv run python bot.py
    


### Angel Code here
RUN mkdir -p /root/angel
WORKDIR /root/angel/
RUN git clone https://github.com/ThetaGainer/dockerangel
WORKDIR /root/angel/dockerangel/research/

EXPOSE 587/tcp

## Last command
ENTRYPOINT /bin/zsh
