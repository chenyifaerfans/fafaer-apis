FROM python:3.6

LABEL maintainer="YING WANG <864891814@qq.com>"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt

WORKDIR /fafaerapis

COPY apps /fafaerapis/apps
COPY fafaerapis /fafaerapis/fafaerapis
COPY extra_apps /fafaerapis/extra_apps
COPY manage.py requirements.txt start.sh /fafaerapis/

RUN pip install -r /tmp/requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com \
    && pip install uwsgi -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9001

CMD "./start.sh"
