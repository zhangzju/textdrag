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

enList = open('err.txt', 'r')
ptList = open('source/err_pt.txt', 'r')
enStr = read_file_as_str('source/err.js')

rows = 747

for index in range(rows):
    enLine = enList.readline().replace("&","\&")
    ptLine = ptList.readline().replace("\"","").replace("&","\&")
    if enLine == ptLine:
        pass
    else:
        cmd = "sed -i 's/"+wrap_texp_with_quote(enLine)+"/"+wrap_texp_with_quote(ptLine)+"/'"+" err.js"
        print(cmd)
        os.system(cmd)
        # print(ptLine)


