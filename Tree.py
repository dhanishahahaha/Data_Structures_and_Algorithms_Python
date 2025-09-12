'''Tree

--> A tree is defined as a finite set of one or more data items such that there is a special node called the
    root node and the remaining nodes are partitioned into n>=0 disjoint subsets of which is itself a tree, 
    and they are known as Subtrees.

--> A tree is a non-linear and Hirarchical data structure. 
--> Binary Tree - A tree with a maximum degree of 2
    
--> Common terms:-
    a) Root node - Main node or first node from which all other branches emerge.
    b) leaf nodes/Terminal nodes - last nodes of the tree with degree zero.
    c) Degree of nodes - No. of nodes emerging from a particular node.
    d) Degree of a tree - The highest degree of a node in the tree is the degree of the tree.
    e) Levels/Generations - Group of nodes from every parent node in the hirarchy.
    f) Path - Connection of nodes excluding the leaf node.
    g) Branch - Connection of nodes including the leaf node.
    h) Height/Depth of the tree - No. of the nodes in the largest branch OR Total no. of generations.

    
Binary Tree - A binary tree is defined as a finite set of elements called nodes such that 
(a) the tree is empty or
(b) it contains a distinguished node R called the root of the tree(T) and the remaining nodes of T form an 
ordered pair of disjoint binary trees T1 and T2.

--> Any node in the Binary tree has 0,1,or 2 child nodes.

--> types of Binary Tree: a) Complete Binary Tree - All levels are completely filled.
                          b) Almost Complete Binary Tree - All levels are completely filled except the last level
                             and the nodes in the last level are left aligned.
                          c) Strict Binary Tree - Each node in this type of tree have only 0 or 2 children nodes.

--> Representation of a Binary Tree: a) Array Representation
                                     b) Linked Representation (by default)

--> We can't do implementation of Binary Tree because for every developer the insertion, deletion and other
    implementation methods can differ so for unique solutions, we work on specific versions of Binary Tree.
--> One of the version of Binary Tree is "Binary Search Tree".


Binary Search Tree - One of the most important data structures, it enables one to search and find for an element
with the average running time with complexity f(n) = O(log2n)

--> In BST, to find or search for a particular element we don't have to n comparisions unlike SLL which makes
    searching very efficient in BST.

--> Even in the worst case scenarios where the element is not found , we do not have to make n comparisions but
    log2n comparisions (i.e 10 for 1000 elements).

--> By default, Duplicate values are not allowed in BST.
--> In BST, all smaller elements are placed on the left side of the node or in the left subtree and all equal 
    or larger values are placed in the right side of the node or the right subtree.

--> Implementation in the BST:- 1) Node - every node in BST has left,item,right
                                2) Insertion - for every element we start from the root node and insert on the basis of comparision of elemets from the nodes in left or right subtrees.
                                3) Search
                                4) Traversing - Preorder (root, Left Tree, Right Tree) , Inorder (Left Tree,Root, Right Tree) , PostOrder (Left Tree, Right Tree, Root) --> InOrder gives sorted elements
                                5) Deletion - possible cases in deletion are a) No child, b) single child, c) two children


'''

#Implementation of Binary Search Tree

'''
--> Define a class Node. The item is used to hold the data,left and right var are used to refer the child nodes.
--> Define a class BST. Make init method to create root var to hold the ref of the root node.
--> Define an insert method to store new data in BST.
--> Define a search method to find a particular item in the BST and return None if the search failed.
--> Define a method to implement inorder traversing in BST.
--> Define a method to implement preorder traversing in BST.
--> Define a method to implement postorder traversing in BST.
--> Define a method to find maximum and minimum value item node.
--> Define a method to delete an item from the Binary search tree. 
--> Define a method size to return the number of elements in BST.
'''

class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=self.rinsert(self.root,data)  
    def rinsert(self,root,data):  #root of subtree
        if root is None:
            return Node(data)
        elif data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        return root
    
    def search(self,data):
        return self.rsearch(self.root,data) 
    def rsearch(self,root,data): #subtree root
        if root is None or root.item==data:  #to match a data and item
            return root
        if data<root.item:
            return self.rsearch(root.left,data) #to move in left subtree
        else:
            return self.rsearch(root.right,data) #to move in right subtree
        
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:  #only runs this if not None
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)

    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:  #only runs this if not None
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:  #only runs this if not None
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)

    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return None
        if data<root.item:
            root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                
    




        