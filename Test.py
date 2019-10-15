#! usr/bin/python3
#-*- encoding: utf-8 -*-

import datetime
from datetime import *

str_date = 'Friday 06 09 2019'
str_a = datetime.strptime(str_date, '%A %d %m %Y')
str_b = datetime.strptime(str_date, '%A %m %d %Y')
print(datetime.strftime(str_a, '%A %d %B %Y'))
print(datetime.strftime(str_b, '%A %d %B %Y'))
print(str_b)