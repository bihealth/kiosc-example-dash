#!/bin/bash

set -euo pipefail


APP_DIR=${APP_DIR-/usr/src/app}
NO_WAIT=${NO_WAIT-0}
export PYTHONUNBUFFERED=${PYTHONUNBUFFERED-1}
HTTP_HOST=${HTTP_HOST-0.0.0.0}
HTTP_PORT=${HTTP_PORT-8050}

cd $APP_DIR
exec gunicorn \
  --bind "$HTTP_HOST:$HTTP_PORT" \
  app:server

exit $?
