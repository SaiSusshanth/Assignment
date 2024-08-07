import random 
from Binary_Search_tree import Binary_Search_Tree

class Tests:

    def __init__(self):
        self.array = [random.randint(0, 1000) for _ in range(2500)]
        self.root = Binary_Search_Tree()
    
    def test_construction_and_traversal(self):
        array = self.array 
        root = self.root

        for value in array:
            root.insert(value)
        
        inorder_traversal = root.inorder_traversal()
        sorted_arr = sorted(array)

        if inorder_traversal == sorted_arr:
            print("No errors with tree construction and traversal")
        else:
            print("Error")
            print(f'Actual: {inorder_traversal}')
            print(f'Expected: {sorted_arr}')
    
    def test_updation_deletion(self):
        array = self.array
        root = self.root

        length = len(array)
        index = random.randint(0, length - 1)
        value = array[index]
        new_value = random.randint(0, 100)
        array[index] = new_value

        root.update(value, new_value)

        inorder_traversal = root.inorder_traversal()
        sorted_arr = sorted(array)

        if sorted_arr == inorder_traversal:
            print("No errors with updation and deletion")
        else:
            print("Errors with updation and deletion")
            print(f'Actual: {inorder_traversal}')
            print(f'Expected: {sorted_arr}')
            print(value, new_value)



if __name__ == '__main__':
    test = Tests()
    test.test_construction_and_traversal()
    test.test_updation_deletion()