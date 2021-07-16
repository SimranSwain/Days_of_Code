import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))


    a = a[d:] + a[:d]   #starts from d and goes upto the length of the array + starts from 0th index and goes upto dth index of the array
    
    print(*a)  #it will print the array with the space separated integers.
     
