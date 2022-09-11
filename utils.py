import graphviz


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

    return hash(tuple(sorted(final)))


def are_isomorphic(graph1, graph2):
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
