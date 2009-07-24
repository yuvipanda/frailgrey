import sys
import os
import shaney
input = sys.argv[1]
count = int(sys.argv[2])
lineno = 1

data = file(input)

def write_file(file_path, data):
    dir = os.path.dirname(file_path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    out = file(file_path, 'w')
    out.write(data)
    out.close()

for line in shaney.generate(data.read(), count):
    write_file(os.path.join('data',str(lineno % 1000), str(lineno))
    if lineno % 100 == 0: 
        print lineno, 'Done'
    lineno += 1
