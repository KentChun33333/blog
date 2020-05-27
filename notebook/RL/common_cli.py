'''description:
this module provide a common_cli tool for run RL experiments

usage:
arg = common_cli.main()

'''

import argparse

def main():
    # input cli variables
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visualize', type=int, default=0,
        help='if input = 1 ; visulizing the plot ')
    parser.add_argument('-l','--logger', type=int, default=0,
        help='if input = 1 ; init the console logger')
    parser.add_argument('-m','--mazeSize', type=int, default=4, 
        help='default 4')
    arg = parser.parse_args()
    return arg 
