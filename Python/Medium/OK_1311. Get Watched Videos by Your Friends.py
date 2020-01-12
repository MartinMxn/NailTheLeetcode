class Solution:
    """
    video watched by your friends, the level 1 is your directly friend, and level > 1 
    so not include you
    
    friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i
    not relation
    """
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        lv = 1
        q = [id]
        visited = set([id])
        res = []
        
        while q:
            n = len(q)
            for i in range(n):
                cur = q.pop(0)  # using the same queue, it has to be pop 1st one, since we keep adding to the last
                for nei in friends[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            lv += 1
            
            if lv == level + 1:
                # pop all watched movie in this level
                # for num in q:
                #     for videos in watchedVideos[num]:
                #         res.add(videos)
                # since it needs to sort by freq
                # Counter would be better here
                movie = []
                for num in q: 
                    movie.extend(watchedVideos[num])
                    
                counter = collections.Counter(movie)
                break
        
        for movie, freq in sorted(counter.items(), key = lambda x: (x[1], x[0])):
            res.append(movie) 
            
        return res
        
