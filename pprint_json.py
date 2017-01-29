import json
import argparse

parser = argparse.ArgumentParser(description='Prettify JSON')
parser.add_argument('json', metavar='DIR', help='path to json')
args = parser.parse_args()


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    readable_json = json.dumps(data, ensure_ascii=False,
                                     sort_keys=True, indent=4)
    print(readable_json)


def main():
    json_content = load_data(args.json)
    pretty_print_json(json_content)


if __name__ == '__main__':
    main()
