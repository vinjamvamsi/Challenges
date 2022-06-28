import requests
import json

metadata_url = "http://169.254.169.254/latest/"
path = ["meta-data/"]

def getmetadata(metadata_url, path):
    result = {}
    for var in path:
        new_url = metadata_url + var
        r = requests.get(new_url)
        text = r.text
        if var[-1] == "/":
            newpath = r.text.splitlines()
            result[var[:-1]] =getmetadata(new_url, newpath)
        elif loadjson(text):
            result[var] = json.loads(text)
        else:
            result[var] = text
    data_to_json = json.dumps(result, indent=2, sort_keys=True)
    print(data_to_json)

def loadjson(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True




if __name__ == '__main__':
    getmetadata(metadata_url, path)
