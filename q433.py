from sys import argv

def dijkstra_score(G, shortest_distances, v, w):
    return shortest_distances[v] + G[v][w]

def dijkstra(G, source):
    unprocessed = set(G.keys()) # vertices whose shortest paths from source have not yet been calculated
    unprocessed.remove(source)
    shortest_distances = {source: 0}

    for i in xrange(len(G) - 1):
        # find a vertex with the next shortest path, i.e. minimal Dijkstra score
        m, closest_head = float('inf'), 0
        for tail in shortest_distances:
            for head in G[tail]:
                if head in unprocessed:
                    d = dijkstra_score(G, shortest_distances, tail, head)
                    if d < m:
                        m, closest_head = d, head

        unprocessed.remove(closest_head)
        shortest_distances[closest_head] = m

    # in case G is not fully connected
    for vertex in unprocessed:
        shortest_distances[vertex] = float('inf')

    return shortest_distances



def main():
    G = get_graph()
    """ Input is adjacency list on vertices labelled 1 to n, including segment length.

    Example line of file:
    1   3,45    92,4

    This means that v. 1 is adjacent to v. 3 with edge length 45 and adjacent to v. 92 with edge length 4.
    """
    source = int(raw_input("Enter source vertex: "))
    destination_vertices = map(int, raw_input("List destination vertices:\n").split())

    distances = dijkstra(G, source)

    print "From vertex %d:" % source
    for vertex in destination_vertices:
        print "The distance to vertex %d is %d." % (vertex, distances[vertex])

if __name__ == '__main__':
    __name__.a
    main()

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        G = self.get_graph(start, bank)

    def get_graph(self, s, b):
        graph = {}
        bank = [s] + b
        for i in bank:
            tmp = []
            for j in bank:
                if i != j and self.judge(i, j):
                    tmp.append(j)
            if tmp:
                graph[i] = tmp
        return graph

    def judge(self, s1, s2):
        return True