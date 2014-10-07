__author__ = 'stephaniehippo'
import sys
from alignment import Alignment

#a = Alignment(1,-1,-2,"atcg","tcg")
#a.global_align()
#a.report_optimal_score()

file = sys.argv[1]
print file
#file = 'test_files/why.txt'
args = open(file).readlines()
flag = args[0].rstrip()
scores = args[1].split()
match = int(scores[0])
mismatch = int(scores[1])
indel = int(scores[2])
seq1= args[2].rstrip()
seq2= args[3].rstrip()

if flag == 'g':
    a = Alignment(match,mismatch,indel,seq1,seq2)
    a.global_align()
    a.report_optimal_score()
elif flag == 'l':
    a = Alignment(match,mismatch,indel,seq1,seq2)
    a.local_align()
    a.report_optimal_score()

else:
    print "Invalid alignment flag."