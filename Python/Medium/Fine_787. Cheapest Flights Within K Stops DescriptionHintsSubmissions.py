class Solution:
    def findCheapestPrice(self, n: int, edges: List[List[int]], start: int, end: int, K: int) -> int:
        """
        build graph to fast look-up price of routes
        defaultdict(dict)
        
        bfs to find the cheapest
        """
        if not edges:
            return 0
        
        graph = collections.defaultdict(dict)
        for s, e, p in edges:
            graph[s][e] = p
        
        best = {}
        pq = [(0, 0, start)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K + 1 or cost > best.get((k, place), float('inf')):
                continue
            if place == end:
                return cost
            
            for nei, price in graph[place].items():
                new_price = cost + price
                if new_price < best.get((k + 1, nei), float('inf')):
                    heapq.heappush(pq, (new_price, k + 1, nei))
                    best[(k + 1, nei)] = new_price
                    
        return -1
        
