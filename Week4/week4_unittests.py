import unittest
from Week4.cyclopeptide_scoring_problem import *

class TestCyclopeptideScoring(unittest.TestCase):
    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            peptide = lines[1]
            spectrum = [int(mass) for mass in lines[2].split(' ')]
            expected = int(lines[4])
        actual = score(peptide, spectrum)
        self.assertEqual(expected, actual)

    def test_sample_dataset(self):
        self._test('DataSets\CyclopeptideScoring\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\CyclopeptideScoring\extra.txt')
