class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        #build graph and do dfs to get all synonyms word.
        graph = collections.defaultdict(set)
        for x, y in synonyms:
            graph[x].add(y)
            graph[y].add(x)
        # "happy"-"joy"-"cheerful"
        # "sad"-"sorrow"
        
        def dfs(word):
            if word in visited:
                return []
            visited.add(word)
            tmp = [word]
            for nxt in graph[word]:
                tmp.extend(dfs(nxt))
            visited.remove(word)
            return tmp
            
        res = [[]]
        visited = set()
        for word in text.split():
            new_res = []
            for lis in res:
                for w in sorted(dfs(word)):
                    new_res.append(lis + [w])
            res = new_res
            
        return map(lambda x: ' '.join(x), res)
            
