"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isPrimeNum(n):
    if (n == 2) or (n == 3):
        return True
    elif (n % 6 != 1) and (n % 6 != 5):
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
    return True

def getPrimeNumCount(n):
    count = 0
    for i in range(2, n + 1):
        if isPrimeNum(i):
            count += 1
    return count

n = int(input())
print(getPrimeNumCount(n))
