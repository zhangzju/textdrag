import re

fd = open('source/help.js', 'r')
line = fd.readline()
pattern = re.compile('"(.*)"')
while line:
    result = pattern.findall(line)
    print(result)