import unittest
from Week3.week3_utility import *
from utilities import AreStringListsEqual

class TestTranslateProtein(unittest.TestCase):

    def test_sample_dataset(self):
        expected = 'MAMAPRTEINSTRING'
        actual = translate_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
        self.assertEqual(expected, actual)

    def test_extra_dataset(self):
        with open('DataSets\ProteinTranslation\extra.txt', 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            rna = lines[1]
            expected = lines[3]
        actual = translate_protein(rna)
        self.assertEqual(expected, actual)


class TestPeptideEncoding(unittest.TestCase):

    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            dna = lines[1]
            peptide = lines[2]
            expected = lines[4:]
        actual = find_peptide_encoding(dna, peptide)
        self.assertTrue(AreStringListsEqual(expected, actual))

    def test_sample_dataset(self):
        self._test('DataSets\PeptideEncoding\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\PeptideEncoding\extra.txt')


class TestTheoreticalSpectrumV1(unittest.TestCase):

    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            peptide = lines[1]
            expected = lines[3]
        actual = ' '.join([str(entry[1]) for entry in cyclospectrum_v1(peptide)])
        self.assertTrue(AreStringListsEqual(expected, actual))

    def test_sample_dataset(self):
        self._test('DataSets\TheoreticalSpectrum\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\TheoreticalSpectrum\extra.txt')


class TestTheoreticalSpectrum(unittest.TestCase):

    def _test(self, data_file_path):
        with open(data_file_path, 'r') as datafile:
            lines = [line.strip() for line in datafile.readlines()]
            peptide = lines[1]
            expected = lines[3]
        actual = ' '.join([str(mass) for mass in cyclospectrum(peptide)])
        self.assertTrue(AreStringListsEqual(expected, actual))

    def test_sample_dataset(self):
        self._test('DataSets\TheoreticalSpectrum\sample.txt')

    def test_extra_dataset(self):
        self._test('DataSets\TheoreticalSpectrum\extra.txt')


class TestPeptideWithGivenMass(unittest.TestCase):

    def test_sample_dataset(self):
        self.assertEqual(14712706211, count_peptide_with_given_mass(1024))

    def test_extra_dataset(self):
        self.assertEqual(34544458837656, count_peptide_with_given_mass(1307))
