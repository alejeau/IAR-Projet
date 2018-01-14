#!/usr/bin/python3
# -*-coding: utf-8 -*

import pprint


def store_text(text: [str], file_name: str):
    with open(file_name, 'w') as results_file:
        for t in text:
            line = str(t) + '\n'
            results_file.write(line)
    results_file.close()


def pretty_store(data: dict, file_name: str):
    pp = pprint.PrettyPrinter(indent=0)
    text = pp.pformat(data)
    with open(file_name, 'w') as results_file:
        results_file.write(text)
    results_file.close()
