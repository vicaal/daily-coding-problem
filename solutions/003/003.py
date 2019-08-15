import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            'val': self.val,
            'left': "#" if self.left == None else self.left.to_dict(),
            'right': "#" if self.right == None else self.right.to_dict()
        }

    @classmethod
    def from_dict(cls, a_dict):
        return Node(
            val=a_dict['val'],
            left=None if a_dict['left'] == "#" else cls.from_dict(a_dict['left']),
            right=None if a_dict['right'] == "#" else cls.from_dict(a_dict['right'])
        )


def serialize(root):
    return json.dumps(root.to_dict())

def deserialize(s):
    return Node.from_dict(json.loads(s))


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

node_1_h1 = Node('root')

#height 2
node_2_h2 = Node('node_2_h2')
node_3_h2 = Node('node_3_h2')

#height 3
node_4_h3 = Node('node_4_h3')
node_5_h3 = Node('node_5_h3')

node_6_h3 = Node('node_6_h3')
node_7_h3 = Node('node_7_h3')

node_1_h1.left = node_2_h2
node_1_h1.right = node_3_h2
node_2_h2.left = node_4_h3
node_2_h2.right = node_5_h3
node_3_h2.left = node_6_h3
node_3_h2.right = node_7_h3

assert deserialize(serialize(node_1_h1)).left.left.val == 'node_4_h3'
