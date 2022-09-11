import numpy as np
import graphviz
import itertools


class Node:
  # TODO: Should probably be immutable

  __slots__ = ['name', 'neighbours', '_label']

  def __init__(self, name, neighbours=''):
    self.name = name
    self.neighbours = neighbours.split()
    
    self._label = self.degree()

  def __repr__(self):
    clsname = type(self).__name__
    return f'{clsname}({self.name}, neighbours={self.neighbours})'

  def __len__(self):
    return len(self.neighbours)

  degree = __len__


class Graph:
  def __init__(self, nodes):
    self.nodes = {node.name: node for node in nodes}

  def __repr__(self):
    clsname = type(self).__name__
    return f'{clsname}({self.nodes!r})'

  def __getitem__(self, key):
    return self.nodes[key]

  def __len__(self):
    return len(self.nodes)


if __name__ == '__main__':
  m = [
      [0, 1, 1, 0],
      [1, 0, 1, 1],
      [1, 1, 0, 0],
      [0, 1, 0, 0]
  ]
  A = Node('A', 'B C')
  B = Node('B', 'A')
  C = Node('C', 'A')

  graph = Graph([A, B, C])
