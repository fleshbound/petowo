#!/bin/bash

PGPASSWORD=${DB_PWD} psql -h ${DB_HOST} -U ${DB_USER} -p ${DB_PORT} --command "create database postgres;"
