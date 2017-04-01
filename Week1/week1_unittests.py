import unittest
from Week1.week1_utility import *
from utilities import AreStringListsEqual

class TestStringComposition(unittest.TestCase):
    def _test(self, datafile_name):
        with open(datafile_name, 'r') as datafile:
            lines = datafile.readlines()
            k = int(lines[1].strip())
            text = lines[2].strip()
            expected_compositions = [line.strip() for line in lines[4:]]

        compositions = string_composition(k, text)
        self.assertTrue(AreStringListsEqual(expected_compositions, compositions))

    def test_extra_dataset(self):
        self._test('Datasets/StringComposition/extra.txt')

    def test_sample_dataset(self):
        self._test('Datasets/StringComposition/sample.txt')


class TestStringSpelledByAGnomePath(unittest.TestCase):
    def _test(self, datafile_name):
        with open(datafile_name, 'r') as datafile:
            lines = datafile.readlines()
            patterns = [line.strip() for line in lines[1:-2]]
            expected_gnome_path = lines[-1].strip()

        gnome_path = string_spelled_by_a_genome_path(patterns)
        self.assertTrue(expected_gnome_path == gnome_path)

    def test_extra_dataset(self):
        self._test('Datasets/GnomePath/extra.txt')

    def test_sample_dataset(self):
        self._test('Datasets/GnomePath/sample.txt')
