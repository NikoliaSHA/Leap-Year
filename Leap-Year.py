#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2015-11-12 20:23:32
# @Authors : Nikolia
# @Python  : 3
print('++++++ Leap-Year +++++++')
Year = int(input('enter the year: '))
if 1900 <= Year <= 3000:
    if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        print('leap year')
    else:
        print('normal year')
else:
    print('enter from 1900 to 3000!')