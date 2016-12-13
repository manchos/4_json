import json
import os


def load_data(filepath: object) -> object:
    """Return the dictionary of bars."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='utf8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    filepath = input('Enter the real path to json file with list of bars:')
    jsonparsed = load_data(filepath)
    pretty_print_json(jsonparsed)

