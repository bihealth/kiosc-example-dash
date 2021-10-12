#!/bin/bash

set -euo pipefail


APP_DIR=${APP_DIR-/usr/src/app}
export PYTHONUNBUFFERED=${PYTHONUNBUFFERED-1}

cd $APP_DIR
exec python app.py
exit $?
