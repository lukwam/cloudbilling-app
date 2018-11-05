# cloudbilling-app
Cloud Billing App - App Engine

## Install

Download the source:

`git clone https://github.com/lukwam/cloudaccounts-app`

Set your Google Cloud Platform project:

`gcloud config set project PROJECT_NAME`

Deploy the app:

`gloud app deploy`

Visit the app:

https://PROJECT_NAME.appspot.com/

## Run Locally

Download a p12 key for your appengine service account:

```shell
gcloud iam service-accounts keys create \
    --key-file-type p12 \
    --iam-account PROJET_NAME@appspot.gserviceaccount.com \
    service_account.p12
```

Convert p12 key to pem for dev_appserver.py:

```shell
cat service_account.p12 | \
    openssl pkcs12  -nodes -nocerts -passin pass:notasecret | \
    openssl rsa > service_account.pem
```
