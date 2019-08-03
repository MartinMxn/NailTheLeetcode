class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        # edges set for fast look-up
        red_set = collections.defaultdict(set)
        blue_set = collections.defaultdict(set)
        for i, j in red_edges:
            red_set[i].add(j)
        for i, j in blue_edges:
            blue_set[i].add(j)
        
        # prevent the iterate cycle
        visited = set()
        visited.add((0, 'red'))
        visited.add((0, 'blue'))
        
        res = [-1] * n
        res[0] = 0
        
        # print(r, b, visited, res)
        step = 0
        
        # check path started from red and blue
        q = [(0, 'red'), (0, 'blue')]
        
        while q:
            step += 1
            tmp_q = []
            while q:
                node, color = q.pop()
                if color == 'red' and node in red_set:
                    for n in red_set[node]:
                        if (n, 'blue') not in visited:
                            visited.add((n, 'blue'))
                            tmp_q.append((n, 'blue'))
                            if res[n] == -1:
                                res[n] = step
                elif color == 'blue' and node in blue_set:
                    for n in blue_set[node]:
                        if (n, 'red') not in visited:
                            visited.add((n, 'red'))
                            tmp_q.append((n, 'red'))
                            if res[n] == -1:
                                res[n] = step
            q = tmp_q
        
        return res
        
        
