__author__ = 'stephaniehippo'
import numpy
from solution import Solution
class Alignment:

    def __init__(self, match, mismatch, indel, seq1, seq2):
        self.match = match
        self.mismatch = mismatch
        self.indel = indel
        self.seq1 = seq1
        self.seq2 = seq2
        self.alignment_matrix = numpy.zeros((len(seq1)+1,len(seq2)+1))
        self.trace_back_matrix = numpy.zeros((len(seq1)+1,len(seq2)+1))
        self.optimal_solution_count = 0

    def initialize_alignment_matrices(self):
        i = 0
        j = 0
        for slot in self.alignment_matrix[0]:
            self.alignment_matrix[0][i] = self.indel * i
            i = i + 1
        for slot in self.alignment_matrix:
            self.alignment_matrix[j][0] = self.indel * j
            j = j + 1
        i = 0
        j = 0
        for slot in self.trace_back_matrix[0]:
            self.trace_back_matrix[0][i] = self.indel * i
            i = i + 1
        for slot in self.trace_back_matrix:
            self.trace_back_matrix[j][0] = self.indel * j
            j = j + 1

    def global_align(self):
        self.initialize_alignment_matrices()
        for i,row in enumerate(self.alignment_matrix):
            if i != 0:
                for j,element in enumerate(row):
                    if j!= 0:
                        score = 0
                        if self.seq1[i-1] == self.seq2[j-1]:
                            score = self.match
                        else:
                            score = self.mismatch
                        left = self.alignment_matrix[i][j-1] + self.indel
                        upper = self.alignment_matrix[i-1][j] + self.indel
                        diagonal = self.alignment_matrix[i-1][j-1] + score
                        optimal_choice = max([left, upper, diagonal])
                        self.alignment_matrix[i][j] = optimal_choice
                        path = []
                        if optimal_choice == left:
                            self.trace_back_matrix[i,j] = -1
                        elif optimal_choice == upper:
                            self.trace_back_matrix[i,j] = 1
                        elif optimal_choice == diagonal:
                            self.trace_back_matrix[i,j] = 0
                        print ""
                    else:
                        print "Skipping first column"
            else:
                print "Skipping first row"

    def single_solution_trace_back(self):
        i = len(self.seq1)
        j = len(self.seq2)
        alnseq1=""
        alnseq2=""
        while i>0 or j>0:
            if self.trace_back_matrix[i,j] == 0:   #diagonal
                alnseq1= alnseq1 + self.seq1[i-1]
                alnseq2= alnseq2 + self.seq2[j-1]
                i = i - 1
                j = j - 1
            elif self.trace_back_matrix[i,j] == -1: #left
                alnseq1=alnseq1 + "-"
                alnseq2=alnseq2 + self.seq2[j-1]
                j = j-1
            else:                                 #up
                alnseq1= alnseq1 + self.seq1[i-1]
                alnseq2= alnseq2 + "-"
                i = i -1
        print alnseq1[::-1]
        print alnseq2[::-1]

    def report_optimal_score(self):
        print "Alignment Matrix"
        print self.alignment_matrix
        print "Traceback Matrix"
        print self.trace_back_matrix
        print "Score"
        print self.alignment_matrix[len(self.seq1)][len(self.seq2)]
        self.single_solution_trace_back()
