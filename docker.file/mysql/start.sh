#!/usr/bin/env bash

/bin/bash mysqld
mysql -uroot -pPa55Word -e "use fafaerapis;source /data/fafaerapis.sql;"