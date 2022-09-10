class Graph:
  def __init__(self, nodes):
    self.adjdict = {n.name: n for n in nodes}
    self._wl_label = None

  def __len__(self):
    return len(self.adjdict)

  def __getitem__(self, key):
    return self.adjdict[key]

  def __repr__(self):
    return f'Graph({self.adjdict!r})'

  def wl_label(self):
    if self._wl_label is not None:
      return self.wl_label
    for _ in range(len(self)):
      new_labels = {}
      for node in self.adjdict.values():
        aggregated = (node.label, tuple(sorted(self[n].label for n in node.neighbours)))
        new_labels[node.name] = hash(aggregated)
      
      for key, val in new_labels.items():
        self[key].label = val
    self._wl_label = hash(n.label for n in self.adjdict.values())
    return self._wl_label

class Node:
  def __init__(self, name, neighbours=''):
    self.name = name
    self.neighbours = neighbours.split()
    self.label = len(self.neighbours)

  def __repr__(self):
    return f'Node({self.name}, neighbours={self.neighbours})'


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

  assert graph1.wl_label() == graph2.wl_label()
  assert graph1.wl_label() != graph3.wl_label()


if __name__ == '__main__':
  test_wl()
