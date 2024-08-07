class TreeNode:
    def __init__(self, value):
        self.left = None 
        self.right = None 
        self.value  = value 


# Has the following functionalities

# insert(val):                  inserts a new node into tree
# search(val):                  returns True if a value is present in the tree
# update(val, new_val):         updates the first occurance of given value to the new value
# delete(val):                  deletes the node with the given value
# preorder_traversal():         Gives the nodes in the order of Node - Left_subtree - Right_subtree
# inorder_traversal():          Gives the sorted order of values

class Binary_Search_Tree:

    def __init__(self):
        self.root = None 

    def insert(self, val):
        node = TreeNode(val)
        root = self.root 

        if root == None:
            self.root = node
            return 
        
        while 1:
            if node.value <= root.value:
                if root.left: root = root.left
                else:
                    root.left = node 
                    break  
            
            else:
                if root.right:
                    root = root.right 
                else:
                    root.right = node 
                    break 

        return
    
    def search(self, value):
        current = self.root 

        while current:

            if current.value == value: return True 

            if value <= current.value:
                current = current.left 
            else:
                current = current.right 

        return False



    def update(self, val, new_val):
        if not self.search(val): return "Value does not exist"

        self.delete(val)
        self.insert(new_val)



    def delete(self, val):
        if not self.search(val):
            return "Value not present in the tree"
        
        return_message = "Value Successfully removed"
        
        parent = None 
        node = self.root 

        while True:
            if val == node.value: break 
            if val <= node.value:
                parent = node 
                node = node.left
            else:
                parent = node 
                node = node.right 
        
        # Case 1: no child
        if node.left == None and node.right == None:

            # node is root node
            if parent == None:
                self.root = None

            elif parent.left == node:
                parent.left = None 
            else:
                parent.right = None 
            return return_message

        # Case 2: one child
        if node.left == None or node.right == None:
            non_null_node = node.right if node.left == None else node.left

            if parent == None:
                self.root = non_null_node 

            elif parent.left == node:
                parent.left = non_null_node
            
            else:
                parent.right = non_null_node
            return return_message
        
        # Case 3: Both child nodes exist
        next_minimum_node = node.right 
        new_parent = node 
        while next_minimum_node.left:
            new_parent = next_minimum_node
            next_minimum_node = next_minimum_node.left

        # Replacing the present node with the next minimum value and removing the next minimum node
        node.value = next_minimum_node.value

        if new_parent.left == next_minimum_node:
            new_parent.left = None 
        else:
            new_parent.right = next_minimum_node.right 
        
        return return_message


    #preorder trversal :        Gives the nodes in the order of Node - Left_subtree - Right_subtree
    def preorder_traversal(self):
        root = self.root 

        if not root: 
            return []
        
        traversal = []
        stack = [root]

        while stack != []:
            node = stack.pop()
            traversal.append(node.value)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return traversal
    

    #inorder traversal :        gives the sorted order of values
    def inorder_traversal(self):
        stack = []
        current = self.root 
        traversal = []

        while current or stack:
            if current != None:
                stack.append(current)
                current = current.left 
                continue 

            current = stack.pop()
            traversal.append(current.value)
            current = current.right
        
        return traversal
            


