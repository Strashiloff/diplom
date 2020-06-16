FROM node:12
RUN echo "deb http://mirror.yandex.ru/debian/ stretch main contrib non-free" > /etc/apt/sources.list
RUN echo "deb http://security.debian.org/debian-security stretch/updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://mirror.yandex.ru/debian/ stretch-updates main contrib non-free" >> /etc/apt/sources.list
RUN apt update; \
    apt install -y apt-utils wget dialog nano zip unzip mc locales iproute2 telnet iputils-ping telnet; \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen; echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen; locale-gen; \
    rm /etc/localtime; ln -s /usr/share/zoneinfo/Asia/Yekaterinburg /etc/localtime
RUN apt install -y apt-transport-https lsb-release ca-certificates;
