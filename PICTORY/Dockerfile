FROM resin/raspberry-pi3-debian:jessie

RUN apt-get update && apt-get install -yq \
   python3 python raspberrypi-bootloader python-pip python3-pip && \
   apt-get install -y curl debian-keyring && \
   sudo gdebi ./pictory_1.1.1-4_all.deb && \
   apt-get install -f && \
   apt-get upgrade && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY . .

ENV INITSYSTEM on

CMD ["gdebi /usr/src/app/src/pictory_1.1.1-4_all.deb"]

