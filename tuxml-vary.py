# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import random

r = lambda: random.randint(0, 255)
r2 = lambda: random.randint(-255, 255)

def mkRandHexColor(): 
    return '#%02X%02X%02X' % (r(), r(), r())

def mkRandTransform(): 
    return 'transform="translate(%d,%d)"' % (r2(), r2()) # % ')"'

regex = r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})"

test_str = open('TuxV1.svg', 'r').read()
matches = re.finditer(regex, test_str)

nstr = re.sub(regex, lambda r: mkRandHexColor(), test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1        
        #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


print(nstr)

#regex2 = r"transform=\"translate(.*)\""
#nstr2 = re.sub(regex2, lambda r: mkRandTransform(), nstr)
#print(nstr2)
