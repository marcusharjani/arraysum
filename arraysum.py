#!/bin/python

import sys

def simpleArraySum(n, ar):
    numbers=0
    answer = sum([int(i) + numbers for i in ar])
    return answer

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
