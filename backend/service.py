import os, shutil, json, subprocess
from flask import jsonify
import pattern.dockerfilepattern as patternfile
import pattern.dockercompose as patterncompose
dirConfig = os.path.abspath('./configs') + '/'

def makeInfrastructure (data):
  lang = data['lang']
  name = data['name']
  version = data['version']
  option = data['option']
  path = os.path.abspath(data['path']) + '/'
  db = data['db']
  password = data['password']
  interface = data['interface']
  
  pathfile = MakeDockerFile (lang, version, option, path)
  pathcompose = MakeComposeFile (path, db, password, interface)
  saveConfig (name, data, pathfile, pathcompose)
  runScript (path, False)
  
def MakeDockerFile (lang, version, option, path):
  lang_pat = ""
  filename = 'Dockerfile'
  
  # Language
  if lang == "python":
    if option != "":
      lang_pat = patternfile.python_add % (version, option)
    else:
      lang_pat = patternfile.python_noadd % version
  elif lang == "php":
    lang_pat = patternfile.php % version
  else:
    lang_pat = patternfile.node % version
    
  strings = [lang_pat, patternfile.base]
  
  writeFile(filename, strings, path)
  return path + filename
  
def MakeComposeFile (path, db, password, interface):
  filename = 'docker-compose.yml'
  db_pat = ""
  strings = []
  if db == "postgres:12":
    db_pat = patterncompose.dbps % password
  else:
    db_pat = patterncompose.dbmy % password
    
  web_pat = patterncompose.web % path
  
  strings.append(patterncompose.base)
  strings.append(web_pat)
  if interface:
    strings.append(patterncompose.adminer)

  strings.append(db_pat)
  strings.append(patterncompose.nginx)
  
  writeFile(filename, strings, path)
  return path + filename
    
def writeFile (name, strings, path):
  direck = path + name
  
  f = open(direck, 'w')
  for string in strings:
    f.writelines(string)
    
  f.close()  

def saveConfig (name, data, pathfile, pathcompose):
  global dirConfig
  filename = 'Config.json'
  path = dirConfig + name + '/'
  
  if not os.path.exists(path):
    os.mkdir(path)
    
  shutil.copy(pathfile, path)
  shutil.copy(pathcompose, path)
  strings = []
  strings.append(json.dumps(data))
  writeFile (filename, strings, path)
  
def getListConfigs ():
  global dirConfig
  tree = os.listdir(dirConfig)
  jsonarray = dict()
  for i in tree:
    path = dirConfig + i +'/Config.json'
    with open(path, 'r') as f:
      data = json.loads(f.read())
    f.close()
    jsonarray[i] = data
  
  return jsonarray

def deleteConfig (data):
  global dirConfig
  name = data['name']
  path = data['path']
  directory = dirConfig + name
  runScript (path, True)
  try:
    os.remove (os.path.abspath(path) + '/' + 'Dockerfile')
  except Exception as e:
    print(e)
  try:
    os.remove (os.path.abspath(path) + '/' + 'docker-compose.yml')
  except Exception as e:
    print(e)
  try:
    shutil.rmtree(directory)
  except Exception as e:
    print(e)

def runScript (path, flag):
  path = os.path.abspath(path)
  print(path)
  if flag:
    p = subprocess.Popen(['./launch_infrastructure.sh', str(path), ''], stdout=subprocess.PIPE)
  else:
    p = subprocess.Popen(['./launch_infrastructure.sh', path, str(flag)], stdout=subprocess.PIPE)
    
  line = p.stdout.readline()
  print(line)
