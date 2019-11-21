class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for child in region[1:]:
                parent[child] = region[0] #trace upward along the tree 
                
        parent_of_reg1 = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            parent_of_reg1.add(region1)
        
        # find lowest common node in tree
        while region2 not in parent_of_reg1: region2 = parent[region2]
            
        return region2
        
        
        
        
                    
        
        
        
