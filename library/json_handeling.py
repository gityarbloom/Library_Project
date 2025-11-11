import json

class JsonHandeling:
  @staticmethod
  def read_json(path):
      with open(path, 'r') as json_file:
        return json.load(json_file)
  
  @staticmethod
  def write_json(path, data:dict ={}):
    with open(path, 'w') as json_file:
      json.dump(data, json_file, indent='\t')

  