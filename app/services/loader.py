import json

def load_json_lines(path: str):
    data = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            data.append(json.loads(line))

    return data