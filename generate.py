import sys
import json
import string
import random

if len(sys.argv) != 4:
    print "Usage: generate.py <x> <y> <output>"
    sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])
output = sys.argv[3]

with open(output, 'w') as f:
    data = []
    idents = [random.choice(list(string.ascii_uppercase))*4 for x in range(x)]
    for ident in idents:
        for x in xrange(y):
            data.append({
                "ident": ident,
                "numeric": 5,
                "float": 99.0,
                "attribute_1": random.choice(list(string.ascii_uppercase))*50,
                "attribute_2": random.choice(list(string.ascii_uppercase))*50,
                "attribute_3": random.choice(list(string.ascii_uppercase))*50,
            })
    f.write(json.dumps({"data": data}))
