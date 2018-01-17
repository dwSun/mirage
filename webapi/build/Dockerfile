FROM python:3.5-alpine
MAINTAINER dwSun

COPY ./requirements.txt /requirements.txt
RUN  apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		xz-dev \
		zlib-dev \
    && pip install -r /requirements.txt\
    && apk del .build-deps \
    && rm -rvf ~/.cache
