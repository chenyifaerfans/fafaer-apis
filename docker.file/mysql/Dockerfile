FROM mysql:5.7

LABEL maintainer="YING WANG<864891814@qq.com>"

COPY ./my.cnf /etc/mysql/conf.d/
COPY ./fafaerapis.sql /data/

EXPOSE 3306

#CMD ["./data/start.sh"]

CMD ["mysqld"]