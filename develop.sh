#!/bin/sh

APP='lukwam-cloudbilling'

dev_appserver.py app.yaml \
    -A ${APP} \
    --admin_host 0.0.0.0 \
    --appidentity_email_address=${APP}@appspot.gserviceaccount.com \
    --appidentity_private_key_path=service_account.pem \
    --enable_host_checking false \
    --host 0.0.0.0 \
    --use_mtime_file_watcher true

