from flask import Flask, redirect, url_for, send_file, request, jsonify, request, send_file, Response, make_response
import sys
import requests
import json
import datetime
import os
import codecs
from os.path import exists
import base64


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
  return send_file('favicon.ico')

@app.errorhandler(404)
def funnyhandler(gay):
  if (request.full_path=="" or request.full_path=="/?" or request.full_path=="/"):
    return "nigaballs221"
  fullpath = request.full_path.replace("/","",1)
  new_url = base64.b64decode(fullpath)
  print(request.headers)
  print(request.method)
  new_url=new_url.decode("ascii")
  print(new_url)
  if (request.method=="GET"):
    redirectresponse = requests.get(new_url, headers=request.headers)
    print(redirectresponse.content)
    return redirectresponse.content
  elif (request.method=="POST"):
    if (request.content_type.startswith('application/json')):
        data = json.dumps(request.json)
    elif (request.content_type.startswith("application/x-www-form-urlencoded")):
      data = request.form
    else:
      data=request.body
    redirectresponse = requests.post(new_url, headers=request.headers,data=data)
    print(redirectresponse.content)
    return redirectresponse.content


if __name__ == "__main__":
  #app.run("0.0.0.0", 8080)
  app.run(host='0.0.0.0', port=8080)