"""
Copyright (c) 2023 Romeo Ahmed. All rights reserved.
Licensed under the MIT license. See LICENSE file in the project root for license information.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d  " % (i, j, i * j), end="")
    print()
