#!/usr/bin/python3
"""
7-add_item module
"""


import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[:]
my_list = []
print(args)
