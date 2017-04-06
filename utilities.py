def AreStringListsEqual(list1, list2):
    if len(list1) != len(list2):
        return False
    for val in list1:
        if val not in list2:
            return False
    for val in list2:
        if val not in list1:
            return False
    return True


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

