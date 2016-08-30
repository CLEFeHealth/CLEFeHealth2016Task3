import sys
from trectools import TrecQrel
filename = sys.argv[1]

tqrel = TrecQrel(filename)
df = tqrel.qrels_data.copy()

def multiply_the_bread(x):
    for a in range(1,7):
        print str(x["query"]) + "00" + str(a), x["q0"], x["filename"], x["rel"]

df.apply(multiply_the_bread, axis=1)

