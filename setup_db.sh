#!/bin/bash
read -p "Mysql password for root:" password
echo "drop database if exists myappdb" | mysql --user=root --password=${password}
echo "create database myappdb" | mysql --user=root --password=${password}
(echo "use myappdb"; cat schema.sql) | mysql --user=root --password=${password}
