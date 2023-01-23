#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time0 = s.split(":")
    if s[-2:] == "PM":
        if time0[0] != "12":
            time0[0] = str(int(time0[0])+12)
    else:
        if time0[0] == "12":
            time0[0] = "00"
    n1time = ':'.join(time0)
    return str(n1time[:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
