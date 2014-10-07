__author__ = 'stephaniehippo'
import sys
from alignment import Alignment

file = sys.argv[1]
#file = 'test_files/test.txt'
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
    a.single_global_single_align()
    a.report_optimal_score()
elif flag == 'l':
    a = Alignment(match,mismatch,indel,seq1,seq2)
    a.local_single_align()
    a.report_optimal_score()
else:
    print "Invalid alignment flag."

file = open('results.txt', "w")
file.write("Score:")
file.write(a.get_optimal_score())
file.write("\n")
file.write("Number of Optimal Alignments:")
file.write(a.get_total_optimal_alignments())
file.write("\n")
file.write("Alignments:")
if flag == 'g':
    file.write(a.single_global_solution_trace_back())
elif flag == 'l':
    file.write(a.single_local_solution_trace_back())
file.close()