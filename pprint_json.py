# -*- coding: utf-8 -*-
import json
import argparse

parser = argparse.ArgumentParser(description='Prettify JSON')
parser.add_argument('json', metavar='DIR', help='path to json')
args = parser.parse_args()


def load_data(filepath):
    with open(filepath) as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    pretty_json = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
    print(pretty_json)


def main():
    data = load_data(args.json)
    pretty_print_json(data)


if __name__ == '__main__':
    main()
