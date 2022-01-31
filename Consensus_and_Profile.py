import pandas as pd
import numpy as np
from Bio import SeqIO
import os
col_names = []
list_seq = SeqIO.parse("cons.fasta",'fasta')
for seq in list_seq:
    col_names.append(seq.id)
matrix = pd.DataFrame(np.empty((0, len(col_names))))
matrix.columns = col_names
pos = 0
for i in SeqIO.parse("cons.fasta",'fasta'):
    col = matrix.columns[pos]
    matrix[col] = np.array(i.seq)
    pos = pos+1
profile_m = pd.DataFrame(columns=['A','C','G','T'])
count_A = 0
count_C = 0
count_G = 0
count_T = 0
row_count = matrix.shape[0]
for num in range(0,row_count):
    for name, values in matrix.iteritems():
        count_A = count_A+values[num].count('A')
        count_C = count_C+values[num].count('C')
        count_G = count_G+values[num].count('G')
        count_T = count_T+values[num].count('T')
        profile_m.loc[num, 'A'] = count_A
        profile_m.loc[num, 'C'] = count_C
        profile_m.loc[num, 'G'] = count_G
        profile_m.loc[num, 'T'] = count_T
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
profile_m_T = profile_m.T
profile_m = profile_m.astype('int')
cons_list = profile_m.idxmax(axis=1)
(list(cons_list))
cons_str=''.join(cons_list)
cons_str


profile_m_T.to_csv('profilematrix.csv',header=False)
print(cons_str)