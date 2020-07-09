import os
import sentry_sdk

from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://3864b7b5f7a04a458b434152ccd01ea1@o417300.ingest.sentry.io/5316483", 
    integrations=[BottleIntegration()]
)

@route("/")  
def index():  
    return 'welcome!'

@route("/success")  
def index():  
    return 'success!'

@route("/fail")  
def error():
    raise RuntimeError("There is an error!")
    return

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
