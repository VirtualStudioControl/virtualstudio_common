import json

from .filewriter import writeFile, readFile

def writeJSON(path : str, values : dict):
    content = json.dumps(values, indent=2)
    writeFile(path, content)

def readJSON(path : str) -> dict:
    content = readFile(path)
    return json.loads(content)