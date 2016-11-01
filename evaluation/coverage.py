from __future__ import division
import pandas as pd


number_of_topics = 66
df = pd.read_csv("coverage.csv", names=["run","missing"])
#df["coverage"] = 100.0 - df["missing"] / 660.0
df["coverage"] = 100.0 * (1. - df["missing"]/660.)


#df["coverage"] = df["coverage"] * 10.0
df["team"] = df["run"].apply(lambda x: x.split(".")[0])
df["runNumber"] = df["run"].apply(lambda x:x.split(".")[1])


df.groupby("team")["coverage"].mean().to_frame("mean_coverage").sort("mean_coverage", ascending=False)


"""
pd.set_option('precision', 3)
df[df["run"].apply(lambda x:"readability_run" in x)][["run","coverage"]]
"""



"""
b = pd.read_clipboard()
from scipy.stats import spearmanr
from scipy.stats import kendalltau

In [60]: spearmanr(b[["Coverage", "P10"]])
Out[60]: (-0.34945054945054943, 0.22068999774644746)

In [61]: spearmanr(b[["Coverage", "uRBP"]])
Out[61]: (-0.21758241758241756, 0.45491937317003273)

In [62]: spearmanr(b[["P10", "uRBP"]])
Out[62]: (0.80219780219780223, 0.00055630561279224327)

In [66]: kendalltau(b["Coverage"], b["P10"])
Out[66]: (-0.23076923076923084, 0.25029107903498626)

In [65]: kendalltau(b["Coverage"], b["uRBP"])
Out[65]: (-0.1428571428571429, 0.47666075457066848)

In [67]: kendalltau(b["P10"], b["uRBP"])
Out[67]: (0.6483516483516486, 0.0012381254741262626)

Team    Coverage    P10 uRBP
GRIUM   99.937229   10  6
KISTI   99.814394   2   8
CUNI    99.601515   3   2
YorkU   99.506061   11  12
Miracl  99.187879   8   11
UBML    98.922727   9   7
ECNU    98.759091   1   1
readability 98.567100   5   3
USST    97.724242   6   9
LIMSI   96.721212   13  14
baseline    96.628788   7   5
HCMUS   96.604167   4   4
KUCS    95.647727   14  13
FDUSGInfo   94.992424   12  10
"""
