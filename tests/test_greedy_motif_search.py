'''
#Test mostprobable.py
#python -m unittest tests.test_greedy_motif_search (under Fan.Biology)
'''
import unittest
from src import greedy_motif_search

class TestGreedyMotifSearch(unittest.TestCase):

    def test_sample_dataset(self):
        dna = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']
        k=3
        t=5
        result = greedy_motif_search.GreedyMotifSearch(dna,k,t)
        output = ['CAG','CAG','CAA','CAA','CAA']
        self.assertEqual(result, output)

    def test_first_occuring(self):
        dna = ['GCCCAA', 'GGCCTG', 'AACCTA', 'TTCCTT']
        k = 3
        t = 4
        result = greedy_motif_search.GreedyMotifSearch(dna, k, t)
        output = ['GCC', 'GCC', 'AAC', 'TTC']
        self.assertEqual(result, output)

    def test_first_kmer(self):
        dna = ['GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC', 'TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC',
               'TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT', 'GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG',
               'GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT','TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT',
               'AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG','AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA']
        k = 5
        t = 8
        result = greedy_motif_search.GreedyMotifSearch(dna, k, t)
        output = ['GAGGC', 'TCATC', 'TCGGC', 'GAGTC','GCAGC','GCGGC','GCGGC','GCATC']
        self.assertEqual(result, output)

    def test_last_kmer(self):
        dna = ['GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT', 'CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT',
               'GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT', 'AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC',
               'ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG']
        k = 6
        t = 5
        result = greedy_motif_search.GreedyMotifSearch(dna, k, t)
        output = ['GTGCGT', 'GTGCGT', 'GCGCCA', 'GTGCCA','GCGCCA']
        self.assertEqual(result, output)

    def test_breaking_ties(self):
        dna = ['GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA', 'TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA',
               'GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA', 'GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC',
               'AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA','AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA',
               'GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA','TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT']
        k = 5
        t = 8
        result = greedy_motif_search.GreedyMotifSearch(dna, k, t)
        output = ['GCAGC', 'TCATT', 'GGAGT', 'TCATC','GCATC','GCATC','GGTAT','GCAAC']
        self.assertEqual(result, output)

    def test_full(self):
        dna = ['GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA', 'TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA',
               'GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA', 'GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC',
               'AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA','AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA',
               'GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA','TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT']
        k = 4
        t = 8
        result = greedy_motif_search.GreedyMotifSearch(dna, k, t)
        output = ['CGCA', 'CGCA', 'GGAG', 'GGCA','GGCA','CGCA','GGTA','GGCA']
        self.assertEqual(result, output)

    def test_dormancy_survival_regulator(self):
        dna = [
            'GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC',
            'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG',
            'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC'
            ,
            'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC'
            ,
            'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG'
            ,
            'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA'
            ,
            'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA'
            ,
            'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG'
            ,
            'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG'
            ,
            'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC'
            ]

        # set t equal to the number of strings in Dna and k equal to 15
        t = len(dna)
        k = 15
        result = greedy_motif_search.GreedyMotifSearch(dna, k, t)
        output = [
            'GTTAGGGCCGGAAGT',
            'CCGATCGGCATCACT',
            'ACCGTCGATGTGCCC',
            'GGGTCAGGTATATTT',
            'GTGACCGACGTCCCC',
            'CTGTTCGCCGGCAGC',
            'CTGTTCGATATCACC',
            'GTACATGTCCAGAGC',
            'GCGATAGGTGAGATT',
            'CTCATCGCTGTCATC'
            ]
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
