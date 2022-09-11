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


def weisfeiler_lehman(graph):
  '''
  Instead of counting number of equal hashes, just return a hash of
  the final labels
  '''
  for _ in range(len(graph)):
    new_labels = {}
    for node in graph.nodes.values():
      aggregated = (node._label, tuple(sorted(graph[n]._label for n in node.neighbours)))
      new_labels[node.name] = hash(aggregated)

    for key, val in new_labels.items():
      graph[key]._label = val

    final = []
    for node in graph.nodes.values():
      final.append(node._label)

    print(tuple(final))

    return hash(tuple(final))
      
    #return hash(n._label for n in graph.nodes.values())


def are_isomorphic(graph1, graph2):
  wl = weisfeiler_lehman
  wl1 = wl(graph1)
  print('---------------')
  wl2 = wl(graph2)
  breakpoint()
  return weisfeiler_lehman(graph1) == weisfeiler_lehman(graph2)


def draw_graph(graph):
  dot = graphviz.Graph(strict=True)
  edge_list = []
  for node in graph.nodes.values():
    dot.node(node.name)
    edges = [f'{node.name}{neighbour}' for neighbour in node.neighbours]
    edge_list.extend(edges)
  dot.edges(edge_list) 
  dot.render(view=True)



def test_wl():
  A = Node('A', 'B C E')
  B = Node('B', 'A')
  C = Node('C', 'A D')
  D = Node('D',' C')
  E = Node('E', 'A B C')
  
  F = Node('F', 'G H J')
  G = Node('G', 'F')
  H = Node('H', 'F I')
  I = Node('I', 'H')
  J = Node('J', 'F G H')

  K = Node('K', 'L M')
  L = Node('L', 'N O')
  M = Node('M', 'K')
  N = Node('N', 'K')
  O = Node('O', 'N L')

  graph1 = Graph([A, B, C, D, E])
  graph2 = Graph([G, H, J, I, F])
  graph3 = Graph([K, L, M, N, O])

  assert are_isomorphic(graph1, graph2)
  assert are_isomorphic(graph1, graph3)

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
  test_wl()
