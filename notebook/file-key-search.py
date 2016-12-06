#! ~/anaconda2/bin/python
# This script let you to search the title of the article in the folder
#

import re
import os
import argparse
import difflib
import numpy as np

def similar(a,b):
    return difflib.SequenceMatcher(None, a, b).ratio()

# =============================================================================
parse = argparse.ArgumentParser()
parse.add_argument('-s', '--search_key', type=str, required=True,
                  help='input the file name to search')
parse.add_argument('-t', '--target_dir', default=os.getcwd(),
                  help='default is your current working dir, or you could assign one')
parse.add_argument('-n', '--numbers_print',type=int, default=5,
                  help='default is 5 search results')
arg = parse.parse_args()

if __name__=='__main__':

    target_dir = arg.target_dir
    search_key = arg.search_key
    print_numbers = arg.numbers_print

    files_list = os.listdir(target_dir)

    similar_key = np.array([similar(x, search_key) for x in files_list ]).argsort()[::-1][:print_numbers]

    for i in similar_key:
        print (files_list[i])










