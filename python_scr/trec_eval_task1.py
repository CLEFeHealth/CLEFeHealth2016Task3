
from trectools import TrecRun, TrecQrel
from trectools import procedures
import glob
import os


task1_run_filepath = "../runs_t1/"
qrels_top = "../qrels/task1.qrels"

filepath = glob.glob(os.path.join(task1_run_filepath, "*.txt"))
topqrels = TrecQrel(qrels_top)

results = []

for filename in filepath:
    r = TrecRun(filename)
    res = r.evaluate_run(topqrels)
    results.append(res)


p10 = procedures.get_results(results, "P_10")
procedures.plot_system_rank("task1_p10.jpg", p10, "P@10")

bpref = procedures.get_results(results, "bpref")
procedures.plot_system_rank("task1_bpref.jpg", bpref, "BPREF")

map_ = procedures.get_results(results, "map")
procedures.plot_system_rank("task1_map.jpg", map_, "MAP")





