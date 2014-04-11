#!/bin/bash
read -p "Mysql password for root:" password
echo "drop database if exists sorbitol" | mysql --user=root --password=${password}
echo "create database sorbitol" | mysql --user=root --password=${password}
(echo "use sorbitol"; cat schema.sql) | mysql --user=root --password=${password}
