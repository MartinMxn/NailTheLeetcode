# Python中的树

### 1. Concept review

#### 1.1 无序树
树中任意节点没有顺序关系，也叫自由树，没啥价值

#### 1.2 有序树

#### 1.2.1 二叉树
节点度最大为2  
完全二叉树：二叉树高度为h，除了最底层，其它层都达到最大的度  
满二叉树： 除了叶节点外每一个节点都有左右子叶且叶子节点都在最底层

#### 1.2.2 平衡二叉树
当且仅当任何节点的两颗子树的高度差不超过1

#### 1.2.3 二分查找树（排序二叉树）
左小右大 可以等于 所有节点子树也同样

Define:
```
class Node(obj):
  """节点类"""
  def __init__(self, val=-1, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
  
class Tree(obj):
  """树类"""
  def __init__(self, root=None):
      self.root = root
   
  def add(self, val):
      node = Node(val)
    
    # if None, assign as root, else add as preorder(NLR)
    if not self.root:
        self.root = node
    else:
        q = []
        q.append(self.root)
        
        while q:
            cur = q.pop(0)
            if not cur.left:
                cur.left = node
                return
            elif not cur.right:
                cur.right = node
                return
            else:
                q.append(cur.left)
                q.append(cur.right)
```

### Preorder/Inorder/Postorder with DFS
```
    def Traversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            # preorder(NLR)
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
            # inorder(LNR)
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
            # postorder(RNL)
            dfs(node.right)
            res.append(node.val)
            dfs(node.left)
            
            # level order
            res = []
            cur_l = [root]

            while cur_l:
                tmp_nodes = []
                tmp_vals = []
                for node in cur_l:
                    tmp_vals.append(node.val)
                    if node.left:
                        tmp_nodes.append(node.left)
                    if node.right:
                        tmp_nodes.append(node.right)
                cur_l = tmp_nodes
                res.append(tmp_vals)
            
            return res
            
        res = []
        dfs(root)
        return res
```
