#!/bin/sh

cat service_account.p12 | openssl pkcs12 -nodes -nocerts -passin pass:notasecret | openssl rsa > service_account.pem
