import re
import os

def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

def wrap_texp_with_quote(str):
    nStr = str.replace("/","\/")
    return "\"" + nStr[:len(str)-1] + "\""

enList = open('help.txt', 'r')
ptList = open('source/help_pt.txt', 'r')
enStr = read_file_as_str('source/help.js')
left = open('helpLeft.txt','w')

rows = 4143

for index in range(rows):
    enLine = enList.readline().replace("&","\&")
    ptLine = ptList.readline().replace("\"","").replace("&","\&")
    if enLine == ptLine:
        pass
    else:
        cmd = "sed -i 's/"+wrap_texp_with_quote(enLine)+"/"+wrap_texp_with_quote(ptLine)+"/'"+" help.js"
        # print(os.system(cmd))
        if os.system(cmd) == 0:
            pass
        else:
            # print(enLine)
            print(ptLine)
            print(enLine+' -- '+ptLine, file = left)
        


