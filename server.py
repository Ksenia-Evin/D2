import os
import sentry_sdk

from bottle import request, route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])

@route('/')  
def index():  
    return 'welcome!'

@route('/success')  
def index():  
    return 'success!'

@route('/fail')  
def error():
    raise RuntimeError("There is an error!")
    return

run(host="localhost", port=8080)