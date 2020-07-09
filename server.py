import os
import sentry_sdk

from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])

app = Bottle()

@app.route('/')  
def index():  
    return 'welcome!'

@app.route('/success')  
def index():  
    return 'success!'

@app.route('/fail')  
def error():
    raise RuntimeError("There is an error!")
    return

app.run(host="localhost", port=8080)