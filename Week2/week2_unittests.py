import unittest
from Week2.week2_utility import *

class TestEulerianCycle(unittest.TestCase):
    def _test(self, datafile_name):
        graph = []
        with open(datafile_name, 'r') as datafile:
            lines = datafile.readlines()
            for line in lines[1:-2]:
                edge_map = line.strip().split(" -> ")
                source = edge_map[0]
                targets = edge_map[1].split(",")
                graph.append([source, targets])
            expected = lines[-1].strip()

        cycle = eulerian_cycle(graph)
        result = '->'.join(cycle)
        if result != expected:
            print("Result:   " + result + "\n")
            print("Expected: " + expected + "\n")
        self.assertTrue(result == expected)

    def test_sample_dataset(self):
        self._test('Datasets/EulerianCycle/sample.txt')

    def test_extra_dataset(self):
        self._test('Datasets/EulerianCycle/extra.txt')


class TestEulerianPath(unittest.TestCase):
    def _test(self, datafile_name):
        graph = []
        with open(datafile_name, 'r') as datafile:
            lines = datafile.readlines()
            for line in lines[1:-2]:
                edge_map = line.strip().split(" -> ")
                source = edge_map[0]
                targets = edge_map[1].split(",")
                graph.append([source, targets])
            expected = lines[-1].strip()

        cycle = eulerian_path(graph)
        result = '->'.join(cycle)
        if result != expected:
            print("Result:   " + result + "\n")
            print("Expected: " + expected + "\n")
        self.assertTrue(result == expected)

    def test_sample_dataset(self):
        self._test('Datasets/EulerianPath/sample.txt')

    def test_extra_dataset(self):
        self._test('Datasets/EulerianPath/extra.txt')

