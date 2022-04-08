#!/usr/bin/python

import sys

for line in sys.stdin:
    print('a')
    line = line.strip()
    fields = line.split(';')
    print(fields)
    temp_med = fields[6]
    id_estacion = fields[2]

    print ('%s\t%s' % (id_estacion, temp_med))