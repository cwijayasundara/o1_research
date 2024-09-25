import json
import os


def safe_write(path, code):
    path = "./software/" + path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w+') as f:
        # if code is a dict then convert this to a string
        if isinstance(code, dict):
            code = json.dumps(code)
        f.write(code)
