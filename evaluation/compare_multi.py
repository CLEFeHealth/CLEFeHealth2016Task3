from __future__ import division
import pandas as pd

dfeng = pd.read_csv("./p10_multi_engqrel.csv", names=["run","p10"])
dfmerged = pd.read_csv("./p10_multi_mergedqrel.csv", names=["run","p10"])

merged = pd.merge(dfeng, dfmerged, on="run", suffixes=["eng","merged"])



