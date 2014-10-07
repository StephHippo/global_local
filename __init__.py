__author__ = 'stephaniehippo'
from alignment import Alignment

a = Alignment(1,-1,-1,"catdr","cate")
a.global_align()
a.report_optimal_score()