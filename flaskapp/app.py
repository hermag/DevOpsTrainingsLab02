import os
import json
import datetime
from flask import Flask
from devopstraininglab02 import *

app = Flask(__name__)

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR=os.path.join(BASE_FOLDER,"test")

@app.route('/')
def hello_world():
    with open(os.path.join(RESOURCE_DIR,"response.json")) as f:
        return "%s %s"%(json.loads(f.read()).get("payload"),datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"),print_age(38)),str(os.uname()[1])

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8088, debug=True)