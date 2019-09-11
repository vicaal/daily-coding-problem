class Node:
    def __init__(self, value):
        self.value = value
        self.both = id(value)


class XORLinkedList:
    def __init__(self, node):
        self.memory = dict()
        self.head = node
        self.head.both = 0
        self.tail = node
        self.tail.both = 0

    def add(self, node):
        self.tail.both ^= id(node.value)
        node.both = id(self.tail.value)
        self.tail = node
        self.memory[id(node.value)] = node

    def get(self, index):
        prev_node_index = 0
        result_node = self.head
        for i in range(0, index):
            next_node_index = prev_node_index ^ result_node.both
            prev_node_index = id(result_node.value)
            result_node = self.memory[next_node_index]
        return result_node

node_a = Node("node_a")
node_b = Node("node_b")
node_c = Node("node_c")
node_d = Node("node_d")
node_e = Node("node_e")

l = XORLinkedList(node_d)
l.add(node_b)
l.add(node_a)
l.add(node_c)
l.add(node_e)

assert l.get(0).value == "node_d"
assert l.get(1).value == "node_b"
assert l.get(2).value == "node_a"
assert l.get(3).value == "node_c"
assert l.get(4).value == "node_e"
