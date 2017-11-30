#!/usr/bin/python3
# -*-coding: utf-8 -*

import pickle


def load(file_name: str) -> dict:
    # Using pickle's deserialization to keep int keys as int
    with open(file_name, 'rb') as data_file:
        results = pickle.load(data_file)
    data_file.close()
    return results
