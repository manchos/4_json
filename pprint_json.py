import json
import os


def load_json_data(filepath: object) -> object:
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    filepath = input('Enter the real path to json file:')
    json_data = load_json_data(filepath)
    pretty_print_json(json_data)

