#!/bin/bash
mongo --host mongodb -u root -p example --eval "db = db.getSiblingDB('test'); db.createCollection('repositories');"
