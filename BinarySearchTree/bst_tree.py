class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Build_BST(arr):
    '''
    Description:
        Build up a Binary Search Tree and return its "root" node.
    
    Parameters:
        arr: <List>
    
    Returns:
        root: <TreeNode>

    '''
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    for num in range(1, len(arr)):
        insert_TreeNode(root, val=arr[num])

    return root

def insert_TreeNode(root, val):
    if not root:
        return TreeNode(val=val)

    if val <= root.val:
        root.left = insert_TreeNode(root.left, val)
    else:
        root.right = insert_TreeNode(root.right, val) 
    
    return root

def delete_TreeNode(root, val):
    if root == None:
        print("It's empty!")
        return 
    if  val < root.val:
        root.left = delete_TreeNode(root.left, val)
    elif val > root.val:
        root.right = delete_TreeNode(root.right, val)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # Find max
        pred = root.right
        while pred != None and pred.left != None:
            pred = pred.left
            
        root.val = pred.val
        root.right = delete_TreeNode(root.right, pred.val)

    return root 



# Traversal: Recursive
def traversal_Preorder_Recursive(root):
    if root:
        print(root.val)
        traversal_Preorder_Recursive(root.left)
        traversal_Preorder_Recursive(root.right)
    
def traversal_Inorder_Recursive(root):
    if root:
        traversal_Inorder_Recursive(root.left)
        print(root.val)
        traversal_Inorder_Recursive(root.right)

def traversal_Postorder_Recursive(root):
    if root:
        traversal_Postorder_Recursive(root.left)
        traversal_Postorder_Recursive(root.right)
        print(root.val)

# Traversal: Iterative
def traversal_Inorder_Iterative(root):
    if not root:
        return
    stack = []
    cur = root
    while True:
        if cur:
            stack.append(cur)
            cur = cur.left
        elif stack:
            cur = stack.pop()
            print(cur.val)
            cur = cur.right
        else:
            break
    return


# Inorder Morris Traversal
def traversal_morris_Inorder(root):
    cur = root
    pred = None

    while cur:
        if cur.left == None:
            print(cur.val)
            cur = cur.right
        else:
            # Find pred
            pred = cur.left
            while pred.right != None and pred.right != cur:
                pred = pred.right
            
            if pred.right == None:
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                print(cur.val)
                cur = cur.right
    return 


if __name__ == "__main__":
    print("######## Structure ##########")
    print("""
                50
               /  \\
              30  70
             / \  /  \\
            20 40     90
    """)
    tree_list = [50,70,90,30,20,40] 
    root = Build_BST(tree_list)
    
    print("######## Recursive Inorder ##########")
    traversal_Inorder_Recursive(root)
    print("######## Iterative Inorder ##########")
    traversal_Inorder_Iterative(root)
    print("######## Morris Inorder ##########")
    traversal_morris_Inorder(root)
    
    print("######## Delete 30 ##########")
    root = delete_TreeNode(root, 30)
    traversal_Inorder_Recursive(root)

    print("######## Delete All ##########")
    tree_list = [50,70,90,20,40]
    for num in tree_list:
        print("######## Delete {0} ##########".format(num))
        root = delete_TreeNode(root, num)
        traversal_Inorder_Recursive(root)
        
    print("######## OverDeleted ##########")
    root = delete_TreeNode(root, 10)
    traversal_Inorder_Recursive(root)
    
    



    
    


