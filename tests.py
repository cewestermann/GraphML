from core import *
from utils import *


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
  assert not are_isomorphic(graph1, graph3)
