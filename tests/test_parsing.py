from fpdfparser.RPDFParser import RPDFParser

p = RPDFParser('testData')
k = p.within_distance_of(23, 23, 50)
for i in k:
    print(0)