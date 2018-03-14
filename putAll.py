import re

enStr = open('source/str.js', 'r')
enList = open('str.txt', 'r')
ptStr = open('source/str_pt.txt', 'r')

rows = 2575

for index in range(rows):
    enLine = enStr.readline()
