#!/usr/bin/env python
import sys
import ujson
import time

# handle command line arguments
if len(sys.argv) != 3:
    print "Usage: ./test_python <input> <output>"
    sys.exit(1)

# read and parse input
read_start = time.time()
with open(sys.argv[1], "r") as f1:
    text = f1.read()
    parse_start = time.time()
    data = ujson.loads(text)
    parse_end = time.time()
read_end = time.time()


# serialize and write output
write_start = time.time()
with open(sys.argv[2], "w") as f2:
    serialize_start = time.time()
    serialized_data = ujson.dumps(data)
    serialize_end = time.time()
    f2.write(serialized_data)
write_end = time.time()

# stats
print "r:" + str(read_end - read_start)
print "p:" + str(parse_end - parse_start)
print "w:" + str(write_end - write_start)
print "s:" + str(serialize_end - serialize_start)
