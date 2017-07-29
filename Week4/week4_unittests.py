import unittest
from utilities import AreStringListsEqual
from Week4.CyclopeptideScoringProblem import score
from Week4.LeaderboardCyclopeptideSequencing import *
from Week4.SpectralConvolutionProblem import spectral_convolution


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


class TestLeaderboardCyclopeptideSequencing(unittest.TestCase):
    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            n = int(lines[1])
            spectrum = [int(mass) for mass in lines[2].split(' ')]
            expected = lines[4].split('-')
        actual = [str(mass) for mass in leaderboard_cyclopeptide(spectrum, n)]
        self.assertTrue(AreStringListsEqual(expected, actual))

    def test_sample_dataset(self):
        self._test('DataSets\LeaderboardCyclopeptideSequencing\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\LeaderboardCyclopeptideSequencing\extra.txt')


class TestTrimLeaderboard(unittest.TestCase):
    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            leaderboard = lines[1].split(' ')
            spectrum = [int(mass) for mass in lines[2].split(' ')]
            n = int(lines[3])
            expected = lines[5].split(' ')
        actual = trim(leaderboard, spectrum, n)
        self.assertTrue(AreStringListsEqual(expected, actual))

    def test_sample_dataset(self):
        self._test('DataSets\TrimPeptideLeaderboard\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\TrimPeptideLeaderboard\extra.txt')


class TestSpectralConvolution(unittest.TestCase):
    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            spectrum = [int(mass) for mass in lines[1].split(' ')]
            expected = lines[3].split(' ')
        actual = [str(mass) for mass in spectral_convolution(spectrum)]
        self.assertTrue(AreStringListsEqual(expected, actual))

    def test_sample_dataset(self):
        self._test('DataSets\SpectralConvolution\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\SpectralConvolution\extra.txt')
