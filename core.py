import numpy as np
import graphviz
import itertools


class Node:

  __slots__ = ['name', 'neighbours']

  def __init__(self, name, neighbours=''):
    self.name = name
    self.neighbours = neighbours.split()

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


def draw_graph(graph):
  dot = graphviz.Graph(strict=True)
  edge_list = []
  for node in graph.nodes.values():
    dot.node(node.name)
    edges = [f'{node.name}{neighbour}' for neighbour in node.neighbours]
    edge_list.extend(edges)
  dot.edges(edge_list) 
  dot.render(view=True)


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
  draw_graph(graph)
