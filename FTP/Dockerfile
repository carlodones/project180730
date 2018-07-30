FROM resin/raspberry-pi3-debian:jessie

RUN apt-get update && apt-get install -yq \
   python3 python raspberrypi-bootloader python-pip python3-pip && \
   apt-get install pure-ftpd && \
   apt-get upgrade && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY . .

ENV INITSYSTEM on


# CMD ["service pure-ftpd restart"]

