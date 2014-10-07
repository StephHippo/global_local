__author__ = 'stephaniehippo'
import numpy
class Alignment:

    def __init__(self, match, mismatch, indel, seq1, seq2):
        self.match = match
        self.mismatch = mismatch
        self.indel = indel
        self.seq1 = seq1
        self.seq2 = seq2
        self.alignment_matrix = numpy.zeros((len(seq1)+1,len(seq2)+1))
        self.trace_back_matrix = {}
        self.optimal_solution_count = 0

    def initialize_alignment_matrices(self):
        i = 0
        j = 0
        for slot in self.alignment_matrix[0]:
            self.alignment_matrix[0][i] = self.mismatch * i
            i = i + 1
        for slot in self.alignment_matrix:
            self.alignment_matrix[j][0] = self.mismatch * j
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
                        left = self.alignment_matrix[i][j-1] + score
                        upper = self.alignment_matrix[i-1][j] + score
                        diagonal = self.alignment_matrix[i-1][j-1] + score
                        final_choice = max([left, upper, diagonal])
                        self.alignment_matrix[i][j] = final_choice
                        self.trace_back_matrix[i,j]=[]
                        if final_choice == left:
                            self.trace_back_matrix[i,j] += [[i,j-1]]
                        if final_choice == upper:
                            self.trace_back_matrix[i,j] += [[i-1,j]]
                        if final_choice == diagonal:
                            self.trace_back_matrix[i,j] += [[i-1,j-1]]
                    else:
                        print "Skipping first row"
            else:
                print "Skipping first row"

    def report_optimal_score(self):
        print self.alignment_matrix
        print self.alignment_matrix[len(self.seq1)][len(self.seq2)]

    #def report_number_solutions(self):
    #
    #
    #def report_traceback(self):
    #    #start at bottom right corner
    #    i=len(self.seq1)
    #    j=len(self.seq2)
    #    solutions = {}
    #
    #    solution_string_seq1 = ""
    #    solution_string_seq2 = ""
    #    while i > 0 and j > 0:
    #        #now we have an array of pairs from which the matrix came from
    #        steps = self.trace_back_matrix[i][j]
    #        if len(steps) == 1:
    #            pair = steps[0]
    #            #if it was diagonal (match) print letter
    #            if pair[0] == i - 1 and pair[1] == j-1:
    #                solution_string_seq1 = seq1[j] + solution_string_seq1
    #                solution_string_seq2 = seq2[i] + solution_string_seq2
    #            #if it was left print dash for seq1 and letter for seq2
    #            elif: pair[0] == i - 1
    #                solution_string_seq1 = "-" + solution_string_seq1
    #                solution_string_seq2 = seq2[i] + solution_string_seq2
    #            #if it was up print dash for seq1 and letter for seq2
    #            elif: pair[1] == j-1
    #                solution_string_seq1 = seq1[j] + solution_string_seq1
    #                solution_string_seq2 = "-" + solution_string_seq2
    #            else:
    #                print "Traceback doesn't actually work."
    #            i = pair[0]
    #            j = pair[1]
    #        else:
    #            self.optimal_solution_count = self.count + len(steps)
    #            for pair in steps:
