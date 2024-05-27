


def traverse_gr(graph):
    return [0, 1, 2, 3]


def m_colouring(graph, count_colours):
    tr = traverse_gr(graph)

    def next_node_fn(node):
        i1 = tr.index(node)
        if i1 >= 3:
            return -1
        return i1 + 1

    def colours_avail_fn(nd, coloured):
        adjacent_nodes = graph.get(nd)
        colours_possible = [i for i in range(1, count_colours+1)]
        colours_not_possible = []
        for adj_nd in adjacent_nodes:
            if coloured.get(adj_nd):
                colours_not_possible.append(
                    coloured.get(adj_nd)
                )
        colours_avail = [
            i1 for i1 in colours_possible
            if i1 not in colours_not_possible 
        ]
        return colours_avail

    def m_col2(node, col_node, coloured):
        answ = False
        coloured[node] = col_node
        next_node = next_node_fn(node)
        if next_node == -1:
            return True
        colours_avail = colours_avail_fn(next_node, coloured)
        if not colours_avail:
            return answ
        for col in colours_avail:
            possible = m_col2(next_node, col, coloured)
            answ = possible or answ
            if answ:
                break
        return answ

    colours = [i for i in range(1, count_colours+1)]
    dict1 = {}
    solution = False
    for c in colours:
        dict1[tr[0]] = c
        solution = solution or m_col2(tr[0], c, dict1)

    return solution

gr1 = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3],
    3: [0, 2],
}
m = 3
print(m_colouring(gr1, m))