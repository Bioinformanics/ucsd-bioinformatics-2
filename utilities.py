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
    def __init__(self):
        self.value = ""
        self.children = []

class DAG:
    """
    Directed Acyclic Graph
    """
    def __init__(self):
        self.roots = []