#!/usr/bin/python3
# -*-coding: utf-8 -*


def store_text(text: [str], file_name: str):
    with open(file_name, 'w') as results_file:
        for t in text:
            line = str(t) + '\n'
            results_file.write(line)
    results_file.close()
