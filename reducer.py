#!/usr/bin/python
import sys

(last_key, max_val) = (None, 0)

for line in sys.stdin:
    (key, val) = line.strip().split("\t")

    if last_key and last_key != key:
        print ("%s\t%s" % (last_key, max_val))
        (last_key, max_val) = (key, float(val))
    else:
        (last_key, max_val) = (key, max(max_val, float(val)))

if last_key:
    print ("%s\t%s" % (last_key, max_val))