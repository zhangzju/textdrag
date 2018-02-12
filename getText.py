import re

f = open('source/help.js', 'r')
strText = open('help.txt', 'w')
helpContent = f.read()
pattern = re.compile('"(.*)"')
result = pattern.findall(helpContent)
for i in range(len(result)):
    if result[i] == 'name' or result[i] == 'paragraph' or result[i] == 'title':
        continue
    print(result[i])
    strText.write(result[i])
    strText.write("\n")
