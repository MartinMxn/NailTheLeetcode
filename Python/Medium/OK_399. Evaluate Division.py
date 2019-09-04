class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        
        def build_graph(equations, values):
            def add_edge(start, end, value):
                graph[start].append((end, value))
                
            for vertical, value in zip(equations, values):
                start, end = vertical
                add_edge(start, end, value)
                add_edge(end, start, 1 / value)
        
        def find_path(query):
            start, end = query
            if start not in graph or end not in graph:
                return -1.0
            
            q = collections.deque([(start, 1.0)]) # self to self -> self / self is 1.0
            visited = set()
            
            while q:
                first, cur_product = q.popleft()
                if first == end:
                    return cur_product
                visited.add(first)
                for nei, value in graph[first]:
                    if nei not in visited:
                        q.append((nei, value * cur_product))
            
            return -1.0
        
        build_graph(equations, values)
        return [find_path(q) for q in queries]
