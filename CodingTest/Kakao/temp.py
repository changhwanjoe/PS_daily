#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'editDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING source
#  2. STRING target
#

import itertools


def editDistance(source, target):
    sub_num = len(source) - len(target)
    min_num = -1
    count = 0
    for i in range(26):
        count = sub_num
        source_list = cipher(source)
        combi_list = list(itertools.combinations(source_list, len(target)))
        for j in range(len(combi_list)):
            temp_str = ""
            for k in range(len(combi_list[j])):
                temp_str += combi_list[j][k]
            num = dfs(temp_str, target)
            temp_num = sub_num + num

        if min_num == -1:
            min_num = temp_num
        elif num <= min_num:
            min_num = temp_num

        source = cipher_string(source)
    #
    return min_num


def dfs(new_source, target):
    count = 0
    if new_source == target:
        return 0

    else:
        for i in range(len(new_source)):
            if new_source[i] != target[i]:
                count += 2

    return count


def cipher_string(old_string):  # max ciper = 25
    char_list = []
    new_string = ""
    for i in old_string:
        if ord(i) == 122:
            char_list.append('a')
        else:
            char_list.append(chr(ord(i) + 1))
    for j in char_list:
        new_string += j
    return new_string


def cipher(old_string):  # max ciper = 25
    char_list = []
    new_string = ""
    for i in old_string:
        if ord(i) == 122:
            char_list.append('a')
        else:
            char_list.append(chr(ord(i) + 1))
    return char_list
    # for j in char_list:
    #    new_string+=j
    # return new_string


if __name__ == '__main__':
    a= "mqfsnmygrquczhymvkurxfelpeagkisearktnjrcapbuuawnmcrgsfsnusuprtnnzbuvtoemgiohvicsnkqhbgoomupuvjmfzpqp"
    b= "yelitmysnjcfgvvvezaprgaonzkofyqqhfmxseezencanocepyzxocwivnkbjrhcehqlcwsagrfookhiwsrjguzonapppyyodlqx"
    print(editDistance(a, b))