from os.path import dirname, join

try:
    import json
except ImportError as e:
    raise RuntimeError("protocol schema requires json to be installed")

protocol_schema = json.load(open(join(dirname(__file__), 'protocol_schema.json')))
