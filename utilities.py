def AreStringListsEqual(expected, result):
    if len(expected) != len(result):
        _print_list_difference(expected, result)
        return False
    for val in expected:
        if (val not in result) or expected.count(val) != result.count(val):
            _print_list_difference(expected, result)
            return False
    return True


def _print_list_difference(expected, result):
    print("Expected: " + str(len(expected)) + ", " + ' '.join(expected) + "\n")
    print("Result:   " + str(len(result)) + ", " + ' '.join(result) + "\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class DirectedGraph:
    """
    Directed Acyclic Graph
    """
    def __init__(self):
        self.roots = []

    def add_node(self, node):
        if not self.roots:
            self.roots.append(node)
            return

