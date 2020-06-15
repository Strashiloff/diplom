import os, service
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
# from OpenSSL import SSL
# context = SSL.Context(SSL.TLSv1_2_METHOD)

template_dir = os.path.abspath('../frontend/dist/')
static_dir = os.path.abspath('../frontend/dist/')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    data = request.get_json ()
    service.makeInfrastructure (data)
    return jsonify (message = 'False')
  return render_template ('index.html')

@app.route('/list', methods=['POST'])
def listConf ():
  return service.getListConfigs ()

@app.route('/delete', methods=['POST'])
def delete ():
  data = request.get_json ()
  service.deleteConfig (data)
  return jsonify (message = 'False')

