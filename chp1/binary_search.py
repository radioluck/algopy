#!/usr/bin/env python3

import sys


def read_whitelist() :
    pass


def read_input() :
    pass

if __name__ == "__main__" :

    whitelist_file = sys.argv[1]
    whitelist = read_whitelist(whitelist_file)
    input_list  = read_input()
    
    for key in whitelist :
        rank = binary_search(input_list,key)
        if(rank != -1 ) :
            print("{} : {}".format(key,rank))





