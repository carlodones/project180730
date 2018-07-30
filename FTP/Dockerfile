FROM resin/raspberry-pi3-debian:jessie

RUN apt-get update && apt-get install -yq \
   python3 python raspberrypi-bootloader python-pip python3-pip && \
   apt-get install pure-ftpd && \
   apt-get upgrade && \
   groupadd ftpgroup && \
   useradd ftpuser -g ftpgroup -s /sbin/nologin -d /dev/null && \
   mkdir /home/pi/FTP && \
   chown -R ftpuser:ftpgroup /home/pi/FTP && \
   pure-pw useradd upload -u ftpuser -g ftpgroup -d /home/pi/FTP -m && \
   ln -s /etc/pure-ftpd/conf/PureDB /etc/pure-ftpd/auth/60puredb && \
   apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY . .

ENV INITSYSTEM on

CMD ["service pure-ftpd restart"]

