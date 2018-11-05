#!/bin/sh

dev_appserver.py app.yaml \
    --admin_host 0.0.0.0 \
    --enable_host_checking false \
    --host 0.0.0.0

