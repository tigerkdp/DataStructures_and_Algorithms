#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:03:32 2018

@author: kdp

1) Add an item in a binary tree like a BST
2) Add an item in a binary tree like BFS
3) Display the items from a tree
4) Delete node recursively 
5) Delete node recursively Alt
6) Delete node iteratively like BFS
7) Print items only in the left node from leaf to root
8) Print items only in the left node from root to leaf
9) Print only extreme right nodes
10) Print all left nodes
11) Print all right nodes
12) Print pre-order recursively
13) Print preorder iteratively
14) Print in-order recursively
15) Print in-order iteratively
16) Print k-th node in an inorder
17) Print post-oder recursively
18) Print post-order iteratively
19) Level Order Traversal
20) Level Order Traversal line-by-line
21) Level Order in Reverse
22) Print all ancestors of a node recursively
23) Print tree in a spiral order
24) Lowest Common Ancestor of two nodes
25) Size of a tree recursively
26) Size of a tree iteratively
27) Max item in a tree recursively
28) Max item in a tree iteratively
29) Height of a tree recursively
30) Height of a tree iteratively
31) Find a node recursively
32) Find a node iteratively
33) Sum of values recursively
34) Sum of values iteratively
35) Sum of values in each level
36) Level with max sum
37) Vertical sum of all nodes
38) is Leaf Node
39) Sum of all left leaf nodes recursively 
40) Diameter of a tree
41) Number of full nodes iteratively
42) Number of full nodes recurively
42) Number of half nodes iteratively
43) Number of half nodes recursively
44) Number of leaf nodes iteratively
45) Number of leaf nodes recursively
46) Node count at eah level
47) Average of elems at each level
48) Deepest node of the tree
49) Bottom View of the tree
50) Right view of the tree
51) Right view of the tree alt
52) Left view recursively
53) Left view iteratively
54) Top view of the tree
55) Sum Tree of a BT
56) Convert to mirror of the tree
57) Build Binary Tree given list in inorder and preoder
58) Build Binary Tree given list in inorder and level
59) Are two trees structurally same
60) Are two trees mirror of each other

"""

class BinaryNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None
        self.hd = 0  #bottom view
        
class BinaryTree:
    
    preindex = 0
    def __init__(self):
        self.root = None

    #insert like a binary search tree. Only numerical values.
    #recursive. if left is not null. move left when new value is smaller, else add on left side.
    #if right is not null, move right when new value is smaller, else add on right side.
    def add(self, data, node):  
        if self.root is None:
            self.root = BinaryNode(data) 
        else: 
            if data < node.info:                            
                if node.left != None:  
                    self.add(data, node.left)             
                else:
                    node.left = BinaryNode(data) 
                    return
            else:
                if node.right != None:    
                    self.add(data, node.right) 
                else:
                    node.right = BinaryNode(data) 
                    return

    #Insert to make it a complete binary tree - from left to right
    # define queue.  Add root to queue.
    # while queue is not empty, pop the first element. 
    # if popped element's left is null, add new node to left else append to queue.
    # if popped element's right is null, add new node to right else append to queue.
    def add_iter(self, root, data):
        q = []
        newNode = BinaryNode(data)
        if newNode is None:
            print("System Memory Error")
            return
        if root is None:
            self.root = newNode
            return
        q.append(root)
        while q:
            temp = q.pop(0)
            if temp.left is not None:
                q.append(temp.left)
            else:
                temp.left = newNode
                return
            if temp.right is not None:
                q.append(temp.right)
            else:
                temp.right = newNode
                return
        del q
        return
    
     #recursively display binary tree
     #call right node with level +1. 
     #print an empty line
     #print empty space for each level.
     #print value
     #call left node with level + 1
    def display(self, p, level):
        if p is None:
            return
        self.display(p.right, level+1)
        print()
        
        for i in range(level):
            print(" ", end=" ")
        print(p.info)
        self.display(p.left, level+1)
   
    """
        16
    
      15
    
        12
    
    10
    
        6
    
      5
    
        4

    """    
        
    #recursively delete a node
    #like a BST deletion.
    def deleteNode(self, p, key):
        
        if p == None:
            return self.root
        
        if key < p.info: 
            p.left = self.deleteNode(p.left, key)
        elif key > p.info:   
            p.right = self.deleteNode(p.right, key)
        else:  #if equal to root.
            #key to be deleted is found
            
            #has two children
            if p.left is not None and p.right is not None:    
                s = p.right  
                while s.left is not None:  #inorder successor
                    s = s.left    
                p.info = s.info #copy the inorder succ node to the key
                p.right = self.deleteNode(p.right, s.info) #call delete on right child
                
            else: #1 child or no child
                if p.left is not None:  #only left child 
                    ch = p.left         #set p.left to child
                else: #only right child or no child
                    ch = p.right
                p = ch
                  
        return p
    

    # recursively delete the tree.
    def delete_binary_tree_rec(self, root):
        if root is None:
            return
        
        if root.left is not None:
            self.delete_binary_tree_rec(root.left)
        if root.right is not None:
            self.delete_binary_tree_rec(root.right)
            
        self.root = None
        return self.root
        
    #Level order traversal. set p to None when there are no leaves. 
    # add root to queue.
    #while queue is not empty, pop first element.
    # if popped elements left exists, add to queue
    # if popped elements right exists, add to queue
    # set popped element to None.
    def _delete_binary_tree_iter(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            p = q.pop(0)
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
            p = None
        return p
    
    def delete_tree_iter(self, node_ref):
        node_ref = self._delete_binary_tree_iter(node_ref)
        return node_ref
    
    # TRAVERSAL METHODS-------------------------------------------------------
    
    
    #recursive - only extreme left nodes in reverse using recurson
    
    def only_extreme_left(self, root):
        if root is None:
            return 
        self.only_extreme_left(root.left)
        print(root.info, end=" ")
       
    """
    Only print extreme left nodes in reverse
    4 5 10 None
    """

    #print only extreme left notes with root first using recursion
    def only_extreme_left_str(self, root):
        if root is None:
            return 
        print(root.info, end=" ")
        self.only_extreme_left_str(root.left)
        
    """
    Only print extreme left starting from root
    10 5 4 None
    """
        
    #print only extreme right nodes in reverse using recursion
    def only_extreme_right(self, root):
        if root is None:
            return 
        self.only_extreme_right(root.right)
        print(root.info, end=" ")
        
    """
    Only print extreme right in reverse
    16 15 10 None
    """
        
    #all left nodes 
    def all_left_nodes(self, root, node_type):
        if root is None:
            return 
        if node_type == 'L':
            print(root.info, end=" ")  
            
        self.all_left_nodes(root.left, "L")
        self.all_left_nodes(root.right, "R")
        
    """
    All left nodes
    10 5 4 12 None
    """
        
    #all right nodes including root
    def all_right_nodes(self, root, node_type):
        if root is None:
            return 
        if node_type == 'R':
            print(root.info, end=" ")  
            
        self.all_right_nodes(root.left, "L")
        self.all_right_nodes(root.right, "R")
        
    """
    All right nodes
    10 6 15 16 None
    """
  
    #recursive - print root.info, call with left node. call with right node
    def pre_order_rec(self, root):
        if root is None:
            return
        print(root.info,  end = " ")
        self.pre_order_rec(root.left)
        self.pre_order_rec(root.right)
        
        """      
                  1                           
              2       3                
          4     5  6     7
          
          preorder is 1, 2, 4, 5, 3,  6, 7
          
          print 1 
              call recursive - make 2 as root (1's left)
              print 2
              call recursive - make 4 as root (2's left)
                  print 4
                      call recursive - make None as root (4's left)
                      return 
                      call recursive - make None as root (4's right)
                      return 
                  return to 2
              call recursive - make 5 as root (2's right)
                  print 5
                      call recursive - make None as root (5's left)
                      return
                      call recursive - make None as root (5's right)
                      return
              return to 2
          return to 1
              call recursive - make 3 as root (1's right)
              print 3
              call recursive - make 6 as root (3's left)
                  print 6
                      call recursive - make None as root (6's left)
                      return
                      call recursive - make None as root (6's right)
                      return
                  return to 3
             call recursive - make 7 as root (3's right)
                 print 7
                     call recursive - make None as root (7's left)
                     return
                     call recursive - make None as root (7's right)
                     return
             return to to 3
          return to 1
         
        """
    
    #stack, add root, 
    #while stack 
        #pop 
        #print p.info, 
        #if right, append right, 
        #if left, append left)        
    def pre_order_iter(self):
        if self.root is None:
            return
        stack = [self.root]

        print("PreOrder Traversal (iter) ", end="-->")
        while stack:
            node = stack.pop()
            print(node.info, end = " " )
            
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
     
    #recursive - call with left, print root.info, call with right         
    def in_order_rec(self, root):
        if root is None:
            return
        self.in_order_rec(root.left)
        print(root.info,  end=" ")
        self.in_order_rec(root.right)
        
    """      
                  1                           
              2       3                
          4     5  6     7
          
        inorder -  4 2 5 1 6 3 7
          
        call function with 1 as root
          call recursive - make 2 as root (1's left)
              call recursive - make 4 as root (2's left)
                  call recursive - make None as root (4's left)
                  return to 4
                  print 4
                  call recursive - make None as root (4's right)
                  return to 4
              return to 2
          print 2
              call recursive - make 5 as root (2's right)
                  call recursive - make None as root (5's left)
                  return to 5
                  print 5
                  call recursive - make None as root (5's right)
                  return to 5
              return to 2
         return to 1
         print 1 
         call recursive - make 3 as root(1's right)
             call recursive - make 6 as root (3's left)
                 call recursive - make None as root(6's left)
                 return to 6
                 print 6
                 call recursive - make None as root (6's right)
                 return to 6
             return to 3
         print 3
             call recursive - make 7 as root(3's right)
                 call recursive - make None as root (7's left)
                 return
                 print 7
                 call recursive - make None as root (7's right)
                 return
             return to 3
         return to 1
        
     return the function call
          
    """
    
    
    #p=root. define stack, 
    #while stack or p, 
        #if p is not None,  (keep adding left nodes until null)
            #append(p), 
            #p=p.left.  
        #else,
            #p=pop(), 
            #print value, 
            #p=p.right
    def in_order_iter(self):
        if self.root is None:
            return
        p = self.root
        stack = []
        print("InOrder Traversal (iter) ", end="-->")

        while stack or p:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                print(p.info,  end=" ")
                p = p.right
                
    """
     3
   2    5
 4   1   
              inorder -  4 2 1 3 5
 
         p = 3
         stack = []
         while stack or p
           if p=3 is not None
              stack = append p=3 [3]
              p = 2, p.left
             
         while stack or p:
            if p = 2 is not none:
                stack = append p = 2  [3,2]
                p = 4, p.left
                
        while stack or p:
            if p = 4 is not None:
                stack = [3,2,4]
                p = None, 4.left, p.left
                
        while stack or p:
            p is None:
            else:
            p = 4 stack.pop, stack [3,2]
            print 4
            p = None. 4.right, p.right
            
        while stack or p:
            p is None
            else:
            p = 2 stack.pop   stack[3]
            print 2
            p = 1, 2.right p.right
            
        while stack or p:
            if p = 1 is not None:
              stack = [3,1]
              p = None, 1.left, p.left
            
        while stack or p:
            p is None
            else:
            p = 1 stack.pop  [3]
            print 1 
            p = None, 1.right, p.right
            
        while stack or p:
            p is none:
            else:
            p = 3, stack.pop  []
            print 3
            p = 5
            p = None. 5.left p.left

        while stack or p: fails.
        return
    """             
                
                
    #p=root. definestack, 
    #while stack or p, if p is not None, append(p), p=p.left.  
    #else,p=pop(), if kth==k print value return, else kth++ p=p.right
    def kth_node_in_order(self, k):
        if self.root is None:
            return
        p = self.root
        stack = []
        print("Kth node in InOrder Traversal (iter) ", end="-->")
        kth = 0
        while stack or p:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if kth == k:
                    print(p.info,  end=" ")
                    return
                else:
                    kth +=1
                p = p.right

    """
    Kth node in InOrder Traversal (iter) -->4 
    
    """
                
    #recursive - call with left, call with right, print root.info        
    def post_order_recur(self, root):
        if root is None:
            return
        self.post_order_recur(root.left)
        self.post_order_recur(root.right)
        print(root.info,  end=" ")
        
    """      
                  1                           
              2       3                
          4     5  6     7
          
    postorder -  4 5 2 6 7 3 1 
          
     call function with 1 as root
         call recursive - make 2 as root (1's left)
             call recursive - make 4 as root (2's left)
                 call recursive - make None as root (4's left)
                 return (root is None)
                 call recursive - make None as root (4's right)
                 return (root is None)
             back to 4
            print 4
        return to 2
            call recursive - make 5 as root (2's right)
                call recursive - make None as root (5's left)
                return (root is None)
                call recursive - make None as root (5's right)
                return (root is None)
            back to 5
            print 5
        return to 2
    return to 1
        call recursive - make 3 as root (1's right)
            call recursive - make 6 as root (3's left)
                call recursive - make None as root (6's left)
                return (root is None)
                call recursive - make None as root (6's right)
                return (root is None)
            back to 6
            print 6
        return to 3
            call recursive - make 7 as root (3's right)
                call recursive - make None as root (7's left)
                return (root is None)
                call recursive - make None as root (7's right)
                return (root is None)
            back to 7
            print 7
        return to 3
        print 3
    return to 1
    print 1
            
        
     return the function call
          
    """      
        
        
    #p=root. 
    #while stack or p. if p is not none, append p to stak, make p=p.left
    #else p=pop(). 
    #if p.right is not none and p.right not in visited set. make p = p.right
     #else add p to visited. print p.info. p = None
    
    def postOrderIter(self, root):
        if self.root is None:
            return
        stack = []
        p = self.root
        visited = set()
        
        print("PostOrder Traversal (iter) ", end="-->")
        while stack or p:
            if p is not None:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if p.right != None and p.right not in visited:
                    stack.append(p)
                    p = p.right
                else:
                    visited.add(p)
                    print(p.info, end=" ")
                    p = None      
  
    
    """      
                  1                           
              2       3                
          4     5  6     7
          
    postorder -  4 5 2 6 7 3 1 

    stack = [],  p = node of 1,  visited = ()

    while stack or p:  
        p != None, p = 1 
        append p  to stack = [1], visited = ()
        now set p = 2  (1.left) 
        
        p != None, p=2,  visited = (), stack=[1]
        append 2 to stack = [1, 2]
        now set p = 4 (2.left)
         
        p != None, p = 4, visited = (),  stack = [1,2]
        append 4 to stack = [1,2,4]
        now set p = None  (4.left)
        
        p = None,  
        pop from stack and set it to p = 4.  stack is now [1,2]
        if 4.right != None
            set visited to 4
            print 4...............................................4
            p = None
        
        p = None, visited = (4), stack = [1,2]
        pop from stack and set it to p = 2   stack is now [1]
        if 2.right != None, (5).
            append 2 to stack = [1,2]
            now set p = 5, 2.right
        
        p != None, p = 5, visited = (4), stack = [1,2]
        append p to stack = [1,2,5]
        now p = None, 5.left
        
        p = None, visited(4), stack = [1,2,5]
        pop 5 from stack and set it to p=5.  stack is now [1,2]
        if 5.right is None
            add 5 to visited. Visited is now (4,5)
            print(5)...............................................5
            p = None
            
        p = None, visited = (4,5), stack = [1,2]
        pop from stack and set it to p = 2.  stack is now [1]
        if 2.right which is 5 is not None but it is in Visited:
            add 2 to visited.  Visited is now (4,5,2)
            print(2)..............................................2
            p = None
            
        p = None, visited = (4,5,2), stack = [1]
        pop from stack and set it to p=1, stack is now []
        if 1.right 3 is not None and is not visited
            append 1 to stack. Stack is now [1]
            p = 3. 1.right
            
        p != none. p= 3,  visited = (4,5,2), stack = [1]
        append 3 to stack.  Stack = [1,3]
        p = 6, 3.left
        
        p!= None, p = 6.  visited = (4,5,2), stack = [1,3]
        append 6 to stack.  Stack = [1,3,6]
        p = None. 6.left
        
        p = None. visited = (4,5,2)  stack = [1,3,6]
        pop from stack and set it to p = 6.  Stack is now [1,3]
        if 6.right is None. 
            add 6 to visited. Visited is now (4,5,2,6)
            print 6..............................................6
            p = None
            
        p = None. visited = (4,5,2,6). stack = [1,3]
        pop from stack and set p  to 3.  stack = [1]
        if p.right != not None and 7 is not in visited.
            append 3 to stack. stack is now [1,3]
            p = 7.  3.right
        
        p != none. p=7 visited = (4,5,2,6), stack = [1,3]
        append 7 to stack.  stack = [1,3,7]
        p = None. p.left
        
        p=None. stack = [1,3,7]
        pop from stack and set is to 7. stack = [1,3]
        if 7.right is None
        add 7 to visited. Visited = (4,5,2,6,7)
        print 7.................................................7
        p = None

    
        p = None. stack = [1,3]
        pop from stack and set it to 3. stack = [1]
        if 3.right is not None and 3.right is not in visited = false
        add 3 to visited. Visited = (4,5,2,6, 7,3)
        print 3.................................................3
        p = None
        
        p = None. stack = [1]
        pop from stack and set it to 1.  stack = []
        if 1.right is Not node and 1.right is not in visited = false
        add 1 to visited. Visited = (4,5,2,6,7,3,1)
        print 1.................................................1
        p = none
        
        stack = [] and p = None. Come out of the loop

    """                  
                    

    #add root to queue. pop queue. print info. add left. add right.
    def level_order_traversal(self):
        queue_list = []
        queue_list.append(self.root)
        
        while queue_list:
            popped = queue_list.pop(0)
            print(popped.info, end=" ")
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)

    """
    
    LevelOrder Traversal -->10 5 15 4 6 12 16 
    """
    
    
     #queue. add root.
     # while 1. NodeCount=length(queue) 
     # if nodeCount==0, break
         #while node count is greater than 0. 
         #pop queue, print, add left, add right. 
         #NodeCount--
         #print()
    def level_order_line_by_line(self):
        queue_list = []
        queue_list.append(self.root)
        
        while 1:
            nodeCount = len(queue_list)    #node count will be 1 at level1, 2 at level 2, 4 at level 3 etc.
            if nodeCount == 0:
                break
            
            while nodeCount > 0:
                popped = queue_list.pop(0)   #pop from queue
                print(popped.info, end=" ")
            
                if popped.left is not None:    #add left 
                    queue_list.append(popped.left)
                
                if popped.right is not None:     #add right
                    queue_list.append(popped.right) 
                
                nodeCount -=1       #decrement node count. After all nodes are printed at each level, nodecount will go back to 0
            print()
            
    """
    LevelOrder Traversal line by line
    10 
    5 15 
    4 6 12 16     
    """
            
    #place all popped items from queue in stack. 
    #Print all items from stack for reverse
    def reverse_level_order(self):
        queue_list = []
        queue_list.append(self.root)
        stack = []
        while queue_list:
            popped = queue_list.pop(0)
            stack.append(popped)
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)

        while stack:
            popp = stack.pop()
            print(popp.info, end=" ")
            
    """
    Reverse LevelOrder Traversal
    16 12 6 4 15 5 10       
    """
            
    #recursion. #if root is None. False. 
    #if root.info == item. True
    # if call with left or self.call with right. print(info).return true
    # return false
    def printAllAncestorsRecur(self, root, item):
        if root is None:
            return False
        if root.info == item:
            return True
        if self.printAllAncestorsRecur(root.left, item) or self.printAllAncestorsRecur(root.right, item):
                print(root.info, end= ",")
                return True
            
        return False
    
    """
    Print all ancestors of a node
    15,10,
    
              1
         2        3
      4     5  6     7
      
                          1. PAAR(1, 5)
                         /      left=True
                        /       13.  print 1 
                       /        14. return True
                      /
                     /
         2.  PAAR (2   (1s't left), 5)
              /   left=F,right=True  \
             /   11 print 2             \
            /    12. return True (right) \
           /                              \
          /                                \
    3. PAAR (4,(2's left), 5)            9 PAAR(5, 5)
         / left= F right=F  \            10. if 5==5, ret True
        /      8. ret False  \
       /                      \
      /                        \ 
    4. PAAR(None, 5)       6. PAAR(None, 5)
     5 Return False      7 Return False
        
     
     another way to represent
     
         1. PAAR(1, 5)
             2. PAAR(2, 5)
                 3. PAAR(4, 5) (left)
                     4. PAAR(None, 5)
                        5. return False
                     6. PAAR(none, 5) (right)
                        7. return False
                   left(4) = F, right(5) = F
                   8. return False (from left side)
                 9. PAAR(5, 5) (right)
                     10. if 5==5, retur True
             if left=F or right=T
               11. print 2
               12. return True
        if left=True or right
          13. print 1
          14. return True
                    
    """
        
    
    #stack, queue, append root to q, reverse = True
    #while q: size = len(q)
       #while size. pop stack. if reverse, append stack(popped info) #else print info.  
       #if left exist, append left. if right exist, append right
       #size --. 
       #if reverse. while s: print(stack.pop())
       #reverse = not(Reverse)
    def print_tree_in_spiral_order(self, root):
        if root is None:
            return
        s = []
        q = []
        q.append(root)
        reverse = True
        while q:
            size = len(q)
            while size:
                popped = q.pop(0)
                
                if reverse:
                    s.append(popped.info)
                else:
                    print(popped.info, end= " ")
                
                if popped.left is not None:
                    q.append(popped.left)
                if popped.right is not None:
                    q.append(popped.right)
                size-=1
                    
            if reverse:
                while s:
                    print(s.pop(), end=" ")
            reverse = not(reverse)
            
    """
    Print nodes in a spiral order
    10 5 15 16 12 6 4     
    """
            
    #recursive LCA
    def LCA(self, root, a, b):
        if root is None:
            return root
        if root == a or root == b:
            return root
        left = self.LCA(root.left, a, b)
        right = self.LCA(root.right, a, b)
        if left and right:
            return root
        else:
            if left:
                return left
            else:
                return right
            
            
    """
             1
          2       3       
       4     5  6   7
     9   20      

    LCA for 20 ad 5 is 2. 
    
    
                           1. LCA(1, 20, 5)  
                        /      left =2,     \              
                       /      right=None       \
        2. LCA(2, 20, 5)     29. ret 2          16. LCA(3, 20, 5)
       /  left=20 right=5  \                      / 28 ret None  \        
      /   15.ret 2          \                    /                \
     /                       \                  /                  \
    3.  LCA (4, 20, 5)     13. LCA(5, 20, 5)   17. LCA(6,        23 LCA(7, 20, 5)
    /  12. ret right=20 \   14. Ret 5            20, 5)  \        24 LCA(None, 20,5) 
   /     left=None       \                     /          \             25 Ret None (left) 
  /                       \                   / 22. rNone \       26 LCA(None, 20,5) 
 4. LCA(9, 20, 5)   10.LCA(20,20,5)          /              \           27 Ret None (right)
 |  9. R None   \   11. Ret 20         18. LCA(None,       20. LCA(None,
 | left=None     \                         20,5)            20,5)
 | right=None    |                    19. Ret None          21. Ret None
 5. LCA(None,   7. LCA(None,                
        20, 5)      20, 5)      
 6. Return None     8.Return None

    

   """       
    #print root to left path     
    #path length will be 0 and path is a list []
    def root_to_leaf_paths(self, root, path, pathlen):
        
        if root is None:
            return 
        
        if len(path) > pathlen:
            path[pathlen] = root.info
        else:
            path.append(root.info)
        pathlen +=1 
        
        if root.left is None and root.left is None:
            print(path)
        else:
            self.root_to_leaf_paths(root.left, path, pathlen)
            self.root_to_leaf_paths(root.right, path, pathlen)
         
            
            
    """
    Root to Leaf paths
    [10, 5, 4]
    [10, 5, 6]
    [10, 15, 12]
    [10, 15, 16]
    
    
        Tree
         10
      5       15
  4     6   12   16    


                        1.  RTP (10, [], 0) 
                            if 0 > 0 else path=[10], pathlen=1
                            /                              \
                          /                                 \
           2. RTP(5, [10], 1)                                \ 
                   if 1 > 1 else path=[10,5], pathlen=2      5. RTP(15, [10], 1) 
            /                  \                                 if 1 > 1 else path=[10,5], pathlen=
           /                    \                            |                            |
          /                      \                           6. RTP(12,[10,15],2)         |
 3. RTP(4, [10,5], 2)          4. RTP(6, [10,5], 2)            .                        7. RTP(12,[10,15],2)
  if 2 > 2 else                                                .                        .
      path=[10,5,4],     if 2 > 2 else path=[10,5,6]           print(10,15,12)          .
          pathlen=3                        pathlen=3                                    print(10,15,16)   
  root.left =None                     root.left =None
  root.right =None                    root.right =None
  print([10,5,5])                     print([10,5,5])
 
    """
    
    def has_path_sum(self, root, remaining_weight):
        
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            if remaining_weight == root.info:
                return True
            else:
                return False
        
        #nonleaf
        return self.has_path_sum(root.left, remaining_weight-root.info) or \
            self.has_path_sum(root.right, remaining_weight-root.info)
            

    #AGGREGATED/SIZE METHODS--------------------------------------------------
    
    #call with left + call with right + 1
    def size_recursive(self, p):
        if p is None:
            return 0
        return self.size_recursive(p.left) + self.size_recursive(p.right) +1 
    
    """
    sample tree
           5
       3       2
    4     1  3   
   
   Answer = 6
   
       Recursive Tree 
               1. call SR(5)
             /  l=3, r=2 + 1  \
            /    r=6           16. SR(2)  ------------23.  SR(None) 
           /                      | 25.r1+0+1=2            24. R0
        2. call SR(3)             |       
        /   l=1, r=1 \            |
       /    15. r=3   \           17. SR(3)
       /               \          | 22 r1   \
      /                \          |          \
     /                  \         19. SR(N)    \
    /                    \          19. r 0    20. SR(N)
   /                      \                    21. r 0 
   3 call SR(4)           9 SR (1)
     / 8 R0+0+1\         |  14 r=1  \
    /           \        |           \
 4. SR(None) 6.SR(None) 10.SR(None)   \
5. ret 0     7. ret 0    11 ret 0   12 SR(None)
                                    13. ret 0
                                    
                                    
   another representation

    1. call SR(5)
        2. SR(3) (left)
            3. SR(4) (left)
                4. SR(None) (left)
                5. return 0
                6. SR(None) (right)
                7. return 0
              8. return 0 + 0 + 1 (from left side)
            9. SR(1) (right)
                10. SR(None) (left)
                11. return 0
                12. SR(None) (right)
                13. return 0
            14. return 0+0+1 (from right side)
         15. return left+right+1 = 1+1+1 = 3
        16. SR(2) right
            17. SR(3) left
                18. SR(None) (left)
                19. return 0
                20. SR(None) right)
                21. return 0
             22. return 0 + 0 + 1 (left side)
            24. SR(None) right
            25. return 0
         26. return left+right+ 1 = 1 + 0 + 1=2 (right side)
    27. Return 3 (from step 15) + 2 (from step 26)
    
    answer = 5
   
   """
    
    
    #level order traversal. if popped is not None. size++
    def size_iter(self):
        queue_list = [self.root]
        size = 0
        while queue_list:
            popped = queue_list.pop(0)
            if popped is not None:
                size += 1
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)
            
        #test
        return size
    
    #maxData = root.info.
    #call with left and store result in lres
    #call with right and store result in rres
    #maxData is max of lres, maxData, rres
    def max_rec(self, root):
        if root is None:
            return float("-inf")
        
        maxData = root.info
            
        lres = self.max_rec(root.left)
        rres = self.max_rec(root.right)
        
        maxData = max(max(lres, maxData), max(rres, maxData))
        return maxData
    
    """
    Max elem in the BT (recur) is 16
    
                1
          3        5
     2
    
     Answer = 5
     Recursive Tree
     
           1. max(1), maxData=1
           /  lres=3, rres=5   \
          /   r=5               \
         /                       12. max(5),maxData=5
      2. max(3), maxData=3                |  r5       \
      /  lres=2  11.r3   \                |            \
     / rres=-inf          \              13. Max(None)  16.Max(None)
    /                     9. Max(None)   14. ret -inf   17. ret -inf
  3.max(2),maxD=2         10. ret -inf 
  |  lres=-inf   \
  | rres=-inf     \
  |  8.r=2         |
  |                |
  4.max(None),     |
 5. ret=-inf     6.Max(None)
                 7. ret=-inf
    
    """
    
    #level order. pop, compare with max and update max.
    def max_iter(self):
        if self.root is None: 
            return
        queue_list = [self.root]
        max1 = float("-inf")
        while queue_list:
            popped = queue_list.pop(0)
            if popped.info > max1:
                max1 = popped.info
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)
            
        return max1

    #Max elem in the BT(iter) is 16
    
    
    #max(call with left, call with right) +1
    def height_rec(self, root):
        if root is None:
            return 0
        return max(self.height_rec(root.left), self.height_rec(root.right)) + 1
    
    #Height of the BT(recur) is  3
    
    """
            1
          3        5
     2
    
    answer = 3
    Recursive Tree
    
               1. Height (1) 
           /  lres=2       \
          /   rres=1        \
         /   19. r=3          12. Height(5)
        /                        |        \
        2. Height(3),            |  18=1   \
      /  lres=1    \             |          \
     /  rres=0      \          13. Max(None)  16.Max(None)
    /   11. r2      9. H(None) 14. ret 0      17. 0
   /                10. ret=0
  3. H(2),           
  | lres=0  \
  | rres=0   \
  | 8. r1     |
  |           |
  4.H(None),  |
  5. ret=0    6.H(None)
              7. ret=0
    
    
    """
    
    
    
    #queue. append root. append none.
    #while q pop. 
    #if pop is none. level++. if queue is not empty. append none
    #else: add left add right.
    def height_iter(self):
        level=0
        if self.root is None:
            return
        queue_list = [self.root]
        queue_list.append(None)
        
        while queue_list:
            popped = queue_list.pop(0)

            if popped is None:
                if queue_list:
                    queue_list.append(None)
                level+=1

            else:
                if popped.left is not None:
                    queue_list.append(popped.left)
                if popped.right is not None:
                    queue_list.append(popped.right)
        
        return level
    
    #Height of the BT(iter) is  3
    
    
    #if root.info==date, found. else# call with left. else call with right
    def find_item_rec(self, root, data):
        if root is None:
            return "not found"
        if root.info == data:
            return "found"
        else:
            temp = self.find_item_rec(root.left, data)
            if temp == "found":
                return temp
            else:
                return self.find_item_rec(root.right, data)   
            
    #Search->Item 5 found in the tree
            
    def find_item_iter(self, root, k):
        if root is None:
            return "not found"
        if root.info == k:
            return "found"
        q = []
        q.append(root)
        while q:
            popped = q.pop(0)
            if popped.info == k:
                return "found"
            if popped.left is not None:
                q.append(popped.left)
            if popped.right is not None:
                q.append(popped.right)
        return "not found" 
    
    #Search->Item 10 found in the tree Iter
    
    #root.info + call with left + call with right
    def sum_of_values_recur(self, root):
        if root is None:
            return 0
        return root.info + self.sum_of_values_recur(root.left) + self.sum_of_values_recur(root.right)    

    #Sum of all elems (recur) is  68

    #level order. pop and sum all values
    def sum_of_values_iter(self):
        queue_list = [self.root]
        sum1 = 0
        while queue_list:
            popped = queue_list.pop(0)
            sum1 += popped.info 
            
            if popped.left is not None:
                queue_list.append(popped.left)
                
            if popped.right is not None:
                queue_list.append(popped.right)
            
        return sum1
    
    #Sum of all elems (iter) is  68
    
    #sum of left nodes
    def sum_of_left_leaves_nodes_rec(self, root):
        res = 0
        if root is not None:
            if self.is_leaf_node(root.left):
                res += root.left.info
            else:
                res += self.sum_of_left_leaves_nodes_rec(root.left)
            res += self.sum_of_left_leaves_nodes_rec(root.right)
        return res
    
    #Sum of all left leaves (recur) is  16
    
    #level order. Append root append None. 
    #if popped is none. print sum.
        #if queue, append None. level++
    #else sum+popped.  Add left to queue. Add Right to queue.
    def sum_at_level(self):
        level=1
        if self.root is None:
            return

        qu = [self.root]
        qu.append(None)
        sum1 = 0

        while qu:
            popped = qu.pop(0)
            
            if popped is None:
                print("Sum at level",level, "is", end="->")
                print(sum1)
                sum1=0

                if qu:
                    qu.append(None)
                level+=1

            else:
                sum1+=popped.info

                if popped.left is not None:
                    qu.append(popped.left)
                if popped.right is not None:
                    qu.append(popped.right)
                   
            
    """
    Sum at level 1 is->10
    Sum at level 2 is->20
    Sum at level 3 is->38
    
       10
      /  \
    5     15
   / \   /  \
  4   6 12   16
  
  
       queue = [10, None]
       popped = 10
       
       queue = [None, 5, 15]
       sum  = 10 (+= popped)
       
       popped = None.
       print sum (10) for level 1
       sum = 0 (set)
       
       queue = [5, 15, None]
       popped = 5
       
       queue = [15, None]
       sum = 5 (+=popped)
       
       queue = [15, None, 4, 6]
       popped = 15
       sum = 20, 5+15 (+=popped )            
       
       queue = [None, 4,6,12,16]
       popped = None 
       print sum (20) for level 2
       sum = 0 (set)
       
       queue = [4,6,12,16, None]
       popped  = 4
       sum  = 4 
       queue = [6,12,16 None]
       
       popped = 6
       sum = 10 (4+6)
       queue = [12, 16, None]
       
       popped 12 
       sum = 22 (10+12)
      
       popped 16
       sum = 38 (22+16)
       queue = [None]
       
       popped = None
       print sum (38) for level 3
       
       sum =0
       
       queue is empty
    
    """
    
    #append root, append none
    #if popped is None, sum. if sum > max. set max.
        #if queue, apppend None. level+
    #else sum+popped. add left. add right.
    def level_with_max_sum(self):
        level=1
        if self.root is None:
            return
        qu = [self.root]
        qu.append(None)
        sum1 = 0
        maxSum = float("-inf")
        maxLevel = 0
        while qu:
            popped = qu.pop(0)
            
            if popped is None:
                print("Sum at ",level, "is", end="->")
                print(sum1)
                if sum1 > maxSum:
                    maxSum = sum1
                    maxLevel = level
                sum1=0
                if qu:
                    qu.append(None)
                level+=1
            else:
                sum1+=popped.info
                if popped.left is not None:
                    qu.append(popped.left)
                if popped.right is not None:
                    qu.append(popped.right)
            
        return maxLevel
    
    """
    Sum at  1 is->10
    Sum at  2 is->20
    Sum at  3 is->38
    Level with max sum  3
    """
    
    
    #if root none, return
    #call recursive functtion with again with left, col-1, dict
    #dict[col] += root.info.  or dict[col] = root.info
    #call recursive function with right, col+1
    def vertical_sum(self, root, column, dict1):
       
        if root is None:
            return
        
        #call again with left with column -1
        self.vertical_sum(root.left, column-1, dict1)
        
        #add or update dictionary
        if column in dict1:
           dict1[column] += root.info
        else:
           dict1[column] = root.info
           
        #call again with right with column+1
        self.vertical_sum(root.right, column+1, dict1)
        
    """
    Vertical sum for each column is : 
        {-2: 4, -1: 5, 0: 28, 1: 15, 2: 16}
    """
        
    def is_leaf_node(self, root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        return False
            
    
    #diameter of the tree
    #left height. right height. left diam, rightdiam. 
    #max of height vs diams
    def diameter_of_tree(self, root):
        if root is None:
            return 0
        lef = self.height_rec(root.left)
        rig = self.height_rec(root.right)
        
        leftdiam = self.diameter_of_tree(root.left)
        rightdiam = self.diameter_of_tree(root.right)
        
        return max(lef + rig+1, max(leftdiam, rightdiam))
    
    #Diameter of the tree is  5
    
    """
       4
    3     2
  1   5 6   7
  
  Diam =5 

    
    """
         
    
    
    
    #NODE COUNT METHODS-------------------------------------------------------
    
    #level order. while q, pop. if node.left and node.right exist. count
    def num_of_full_nodes(self, root):
        if root is None:
            return 0
        q = []
        q.append(root)
        count = 0
        while q:
            node = q.pop(0)
            if node.left is not None and node.right is not None:
                count +=1
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return count

    #Num of full nodes  3

    #recursive
    def num_of_full_nodes_rec(self, root):
         if root is None :
             return 0
         res  = 0
         if root.left is not None and root.right is not None:
             res +=1 
         res += self.num_of_full_nodes_rec(root.left) + self.num_of_full_nodes_rec(root.right) 
         return res

    #Num of full nodes (recur):  3

    #level order. count half nodes 
    #left not none. right none, count++
    #right not none, left none, count++
    def num_of_half_nodes(self, root):
        if root is None:
            return 0
        q = []
        q.append(root)
        count = 0
        while q:
            p = q.pop(0)
            if p.left is not None and p.right is None:
                count +=1
            if p.right is not None and p.left is None:
                count +=1
                
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)
        return count
    
    #Num of half nodes  0
    
    
    #recursive half nodes
    def num_of_half_nodes_rec(self, root):
         if root is None :
             return 0
         res  = 0
         if root.left is not None and root.right is None:
             res +=1
         if root.right is not None and root.left is None:
             res +=1
             
         res += self.num_of_half_nodes_rec(root.left) + self.num_of_half_nodes_rec(root.right) 
         return res
     
        #Num of half nodes (recur):  0
    
    #level order. while q. pop.
    #right and left are none. count++
    def num_of_leaf_nodes(self, root):
        if root is None:
            return 0
        q = []
        q.append(root)
        count = 0
        while q:
            node = q.pop(0)
            if node.left is None and node.right is None:
                count +=1
            else:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return count
    
    #Num of leaf nodes  4
    
    #recursive leaf node
    def num_of_leaf_nodes_rec(self, root):
         if root is None :
             return 0
         res  = 0
         if root.left is None and root.right is None:
             res +=1             
         res += self.num_of_leaf_nodes_rec(root.left) + self.num_of_leaf_nodes_rec(root.right) 
         return res    
    
    #Num of leaf nodes (recur)  4
    
    #q, append root. append none.
    #while q, pop. 
    #if popped is none. print count. set count=0. if q, append none. level++
    #else count++, add left, add right.    
    def node_count_at_each_level(self):
        level=1
        if self.root is None:
            return
        queue_list = [self.root]
        queue_list.append(None)
        count1 = 0

        while queue_list:
            popped = queue_list.pop(0)

            if popped is None:
                print("Node Count at level ",level, "is", end="->")
                print(count1)
                count1=0

                if queue_list:
                    queue_list.append(None)
                level+=1

            else:
                count1+=1
                if popped.left is not None:
                    queue_list.append(popped.left)
                if popped.right is not None:
                    queue_list.append(popped.right)
              
    """
    Node Count at level  1 is->1
    Node Count at level  2 is->2
    Node Count at level  3 is->4
    """
            
    #two while loops. two queues.  
    def average_of_elemts_at_each_level(self, root):
        q = []
        q.append(root)
        
        while q:
            sum1 = count = level = 0
            temp = []
            
            while q:
                p = q.pop(0)
                sum1 += p.info
                count+=1
                level += 1
                
                if p.left is not None:
                    temp.append(p.left)
                if p.right is not None:
                    temp.append(p.right)
            q = temp
            print("Sum at each level : ", level, sum1)
            print("Average at level :", level, sum1 / count)

        """
        Sum at each level :  1 10
            Average at level : 1 10.0
        Sum at each level :  2 20
            Average at level : 2 10.0
        Sum at each level :  4 38
            Average at level : 4 9.5
        """

    def deepest_node(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            popped = q.pop(0)
            if popped.left is not None:
                q.append(popped.left)
            if popped.right is not None:
                q.append(popped.right)
        return popped.info

    #Deepest node of the tree iter is 16

    # VIEWS-------------------------------------------------------------------

    #queue, add root. while q. pop(0). hd=popped.hd. update dict[hd] = popped.info
    #if left, left.hd=hf-1, append lefy. #if right right.hd=hd+1, append right.
    #print dictionary
    def bottom_view(self, root):
        if root is None:
            return
        q = []
        ht = {}
        q.append(root)
        while q:
            popped = q.pop(0)
            hd = popped.hd
            ht[hd] = popped.info
            
            if popped.left is not None:
                popped.left.hd = hd -1
                q.append(popped.left)
                
            if popped.right is not None:
                popped.right.hd = hd + 1
                q.append(popped.right)
        
        print(ht)
        
    """
    Bottom View of the tree is 
    {0: 12, -1: 5, 1: 15, -2: 4, 2: 16}
    """
    
    #q, append root. 
    #two while loops. while q. count=len(q). level++. 
        #while count >0, pop. if levl > max_level. print pop.info. max_level=level
        #if right, append.  if left, append.  count--
    def right_view(self, root):
        if root is None:
            return
        
        q = []
        q.append(root)
        level = 0
        max_level = 0
        print("Right View of the binary Tree is :")
        while q:
            count = len(q)
            level +=1 
            while count != 0:
                popped = q.pop(0)
                if level > max_level:
                    print(popped.info, end=" ")
                    max_level = level
                
                if popped.right is not None:
                    q.append(popped.right)
                if popped.left is not None:
                    q.append(popped.left)
                count -=1
   
    """
    Right View of the binary Tree is :
        10 15 16
    """
         
    def right_view_alt(self, root):
        if root is None:
            return
        
        qu = []
        qu.append(self.root)        
        while 1:
            nodeCount = len(qu)    #node count will be 1 at level1, 2 at level 2, 4 at level 3 etc.
            if nodeCount == 0:
                break
            
            while nodeCount > 0:
                popped = qu.pop(0)   #pop from queue                
            
                if popped.left is not None:    #add left 
                    qu.append(popped.left)
                
                if popped.right is not None:     #add right
                    qu.append(popped.right) 
                
                nodeCount -=1       #decrement node count. After all nodes are printed at each level, nodecount will go back to 0
            
            print(popped.info, end=" ")
        
   # 10 15 16 
    
            
    def left_view_rec(self, root):
        max_level = [0]
        self.left_view_util(root, 1, max_level)

    def left_view_util(self, root, level,max_level):
        if root is None:
            return
        if max_level[0] < level:
            print(root.info, end=" ")
            max_level[0] = level
        
        self.left_view_util(root.left, level+1, max_level)
        self.left_view_util(root.right, level+1, max_level)
        
    """
    Left View of the tree (recur) is:
        10 5 4 
    """
    
    def left_view_iter(self, root):
        
        qu = []
        qu.append(self.root)
        
        while 1:
            nodeCount = len(qu)    #node count will be 1 at level1, 2 at level 2, 4 at level 3 etc.
            if nodeCount == 0:
                break
            
            left_node = 1
            while nodeCount > 0:
                popped = qu.pop(0)   #pop from queue                
                if left_node == 1:                        
                    print(popped.info, end=" ")
            
                if popped.left is not None:    #add left 
                    qu.append(popped.left)
                
                if popped.right is not None:     #add right
                    qu.append(popped.right) 
                
                nodeCount -=1       #decrement node count. After all nodes are printed at each level, nodecount will go back to 0
                left_node +=1
                
    #queue, append root. dict. pop. if hd not in ht. add hd=info
    #if left, left.hd-1, append. #if right, right.hd+1, append.
    def top_view(self, root):
        if root is None:
            return
        q = []
        ht = {}
        q.append(root)
        
        while q:
            popped = q.pop(0)
            hd = popped.hd
            
            if hd not in ht:
                ht[hd] = popped.info
            
            if popped.left is not None:
                popped.left.hd = hd-1
                q.append(popped.left)
                
            if popped.right is not None:
                popped.right.hd = hd+1
                q.append(popped.right)
                
        print(ht)
        
    """
    Top View of the tree is 
        {0: 10, -1: 5, 1: 15, -2: 4, 2: 16}
    """
        
    #CONSTRUCTION of other Trees-----------------------------------------------
    def sum_tree(self, root):
        if root is None:
            return 0
        
        old_val = root.info 
        root.info = self.sum_tree(root.left) + self.sum_tree(root.right)
        return root.info + old_val
    
    #recursive conversion to mirror trees
    def convert_to_mirror_of_tree(self, root):
        if root is None:
            return
        if root:
            self.convert_to_mirror_of_tree(root.left)
            self.convert_to_mirror_of_tree(root.right)
            root.left, root.right = root.right, root.left
        return 
    
    """
          5
    
        6
    
    10
    
        12
    
      15
    
        16
    """
    
        
    #select elem from preorder using preindex.     
    #create new node with the data selected from preorderr
    #find the index of the new node element in inorder list
    #call build tree for elem before in_index and make the tree as left tree of newNode
    #call build tree for elem after in_index and make the tree as right subtree of newNode
    #repeat steps 1 to 5 with next index of preindex
    def build_binary_tree_in_pre(self, inorder, preorder, in_start, in_end):
        
        if in_start > in_end:
            return None
        
        #BT2.preindex is a static variable. 
        newNode = BinaryNode(preorder[BT2.preindex])
        BT2.preindex+=1
        
        if in_start == in_end:
            return newNode
        
        in_index = inorder.index(newNode.info)
        newNode.left = self.build_binary_tree_in_pre(inorder, preorder, in_start, in_index-1)
        newNode.right = self.build_binary_tree_in_pre(inorder, preorder, in_index+1, in_end)
        return newNode
    
    """
    Construct BT from level order and inorder sequence in a list

        70
    
      60
    
        55
    
    50
    
        45
    
      40
    
          35
    
    """
    
    #first elem in level order sequence is root. 
    #create a new node with the data selected from level order
    #find the index of the new node elem in inorder list 
    #call build tree for newnode elem before in_index in inorder list and make the tree as left tree of newNode
    #call build tree for newnode elem after in_index in inorder list and make the tree as right tree of newNode
    #repeat steps 1 to 5 with next index of the level order
    def build_binary_tree_in_level(self, level, inorder):
        
        if inorder:
            for i in range(0, len(level)):
                if level[i] in inorder:
                    
                    newNode = BinaryNode(level[i])
                    
                    io_index = inorder.index(level[i])
                    break
                
            if not inorder:
                return newNode
            
            newNode.left = self.build_binary_tree_in_level(level, inorder[0:io_index])
            newNode.right = self.build_binary_tree_in_level(level, inorder[io_index+1 : len(inorder)])
            return newNode

    """
          22
    
    20
    
          14
    
        12
    
          10
    
      8
    
    """

        
    #VALIDATIOON
    def are_structurally_same_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.info == root2.info:
            return True
        return self.are_structurally_same_tree(root1.left, root2.left) and self.are_structurally_same_tree(root1.right, root2.right)

    #Are trees structurally the same:  True

    #same as is_symmetric of each other
    def are_mirror_of_each_other(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.info != root2.info :
            return False
        return self.are_mirror_of_each_other(root1.left, root2.right) and self.are_mirror_of_each_other(root1.right, root2.left)

    #Are trees mirror of each other:  False

    def is_balanced(self, root):
        
        if root is None:
            return True
        left_height = self.height_rec(root.left)
        right_height = self.height_rec(root.right)
        
        if abs(left_height - right_height) <= 1 and \
            self.is_balanced(root.left) and self.is_balanced(root.right):
            return True
        
        return False
    
    #Is the true balanced:  True

#Test:
print("#---------Create Tree instance----------#")
BT = BinaryTree()

print("#---------Add nodes to the tree----------#")
BT.add(10, BT.root)
BT.add(5, BT.root)
BT.add(15, BT.root)
BT.add(4, BT.root)
BT.add(6, BT.root)
BT.add(12, BT.root)
BT.add(16, BT.root)

BT.display(BT.root,0)


#Traversal Methods
print()
print("#----------Traversal Methods----------------#")
print()
print("Only print extreme left nodes in reverse")
print(BT.only_extreme_left(BT.root))     
print()
      

print()
print("Only print extreme left starting from root")
print(BT.only_extreme_left_str(BT.root))     
print()


print()
print("Only print extreme right in reverse")
print(BT.only_extreme_right(BT.root))     
print()

print()
print("All left nodes")
print(BT.all_left_nodes(BT.root, "L"))     
print()


print()
print("All right nodes")
print(BT.all_right_nodes(BT.root, "R"))     
print()


print("PreOrder Traversal (recur) -->", end="")
BT.pre_order_rec(BT.root)
print()
BT.pre_order_iter()

print()
print()
print("InOrder Traversal (recur) -->", end="")
BT.in_order_rec(BT.root)
print()
BT.in_order_iter()

print()
BT.kth_node_in_order(0)

print()
print()
print("PostOrder Traversal (recur) -->", end="")
BT.post_order_recur(BT.root)
print()
#BT.postOrderIter(BT.root)


print()
print()
print("LevelOrder Traversal -->", end="")
BT.level_order_traversal()


print()
print()
print("LevelOrder Traversal line by line")
BT.level_order_line_by_line()

print()
print("Reverse LevelOrder Traversal")
BT.reverse_level_order()

print()
print()
print("Print all ancestors of a node")
BT.printAllAncestorsRecur(BT.root, 12)
print()

print("Print nodes in a spiral order")
BT.print_tree_in_spiral_order(BT.root)
print()

print("Lowest common ancestor of two nodes")
print(BT.LCA(BT.root, 12, 4))
print()


print("Root to Leaf paths")
BT.root_to_leaf_paths(BT.root, [], 0)
print()


print("Has path Sum of 19", BT.has_path_sum(BT.root, 19))
print()

#Aggregate Methods
print()
print("#----------Aggregated Methods--------------#")
print("Max elem in the BT (recur) is", BT.max_rec(BT.root))
print("Max elem in the BT(iter) is", BT.max_iter())

print()
print("Height of the BT(recur) is ", BT.height_rec(BT.root))
print("Height of the BT(iter) is ", BT.height_iter())

print()
print("Deepest node of the tree iter is", BT.deepest_node(BT.root))

print()
print("Search->Item {} {} in the tree".format(5, BT.find_item_rec(BT.root, 5)))
print("Search->Item {} {} in the tree Iter".format(10, BT.find_item_iter(BT.root, 10)))

print()
print("Sum of all elems (recur) is ", BT.sum_of_values_recur(BT.root))
print("Sum of all elems (iter) is ", BT.sum_of_values_iter())

print()
print("Sum of all left leaves (recur) is ", BT.sum_of_left_leaves_nodes_rec(BT.root))

print()
print("Diameter of the tree is ", BT.diameter_of_tree(BT.root))

print()
BT.sum_at_level()

print()
print("Level with max sum ", BT.level_with_max_sum())

print()
BT.average_of_elemts_at_each_level(BT.root)
print()



dict1 = {}
BT.vertical_sum(BT.root, 0, dict1)
print("Vertical sum for each column is : ")
print(dict1)

#Node Count Methods
print()
print("#----------Node Count Methods--------------#")
print("total nodes of the BT (recur) is", BT.size_recursive(BT.root))
print("total nodes of the BT (iter) is", BT.size_iter())

print()
print("Num of full nodes ", BT.num_of_full_nodes(BT.root))
print("Num of full nodes (recur): ", BT.num_of_full_nodes_rec(BT.root))

print()
print("Num of half nodes ", BT.num_of_half_nodes(BT.root))
print("Num of half nodes (recur): ", BT.num_of_half_nodes_rec(BT.root))
print()
print("Num of leaf nodes ", BT.num_of_leaf_nodes(BT.root))    
print("Num of leaf nodes (recur) ", BT.num_of_leaf_nodes_rec(BT.root))

print()
BT.node_count_at_each_level()



# VIEWS
print("#----------View Methods--------------#")
print("Bottom View of the tree is ")
BT.bottom_view(BT.root)
print()

print("Top View of the tree is ")
BT.top_view(BT.root)
print()

BT.right_view(BT.root)
print()

BT.right_view_alt(BT.root)
print()

print()
print("Left View of the tree (recur) is:")
BT.left_view_rec(BT.root)
print()

print("Left view iterative of the tree is: ")
BT.left_view_iter(BT.root)
print()

print()
print("#---------Remove node 4 from the tree------#")
BT.deleteNode(BT.root, 4)
BT.display(BT.root,0)
print()

# CONSTRUCTION METHODS
print("#----------Construction Methods--------------#")
print()
print("Sum Tree")
root = BT.sum_tree(BT.root)  #temporarily commented to test conversion to mirror tree
BT.display(BT.root, 0)

print("Construct BT from inorder and pre-order sequence in a list")
inorder = [20, 30, 35, 40, 45, 50, 55, 60, 70]
preorder = [50,40, 30, 20, 35,45,60,55,70]
BT2 = BinaryTree() 
BT2.preindex = 0
BT2.root = BT2.build_binary_tree_in_pre(inorder, preorder, 0, 8 )
BT2.display(BT2.root, 0)

print("Construct BT from level order and inorder sequence in a list")
levelorder = [20, 8,22,4,12,10,14]
inorder = [4, 8, 10,12,14,20,22]
BT3 = BinaryTree() 
ino_len = len(inorder)
BT3.root = BT2.build_binary_tree_in_level(levelorder, inorder )
BT3.display(BT3.root, 0)


print()
print("Convert BT tree to its mirror")
BT.convert_to_mirror_of_tree(BT.root)
BT.display(BT.root,0)
print()


print("#----------Create another Tree-------------#")
BT1 = BinaryTree()
BT1.add_iter(BT1.root, 10)
BT1.add_iter(BT1.root, 5)
BT1.add_iter(BT1.root, 15)
BT1.add_iter(BT1.root, 4)
BT1.add_iter(BT1.root, 6)
BT1.add_iter(BT1.root, 12)
BT1.add_iter(BT1.root, 16)

BT1.display(BT1.root,0)
BT1.deleteNode(BT1.root, 4)
print()
print("Node 4 removed which had no children. Display Tree again")
BT1.display(BT1.root,0)

print()
BT1.deleteNode(BT1.root, 15) 
print()
print("Node 15 removed which had two rows. Display Tree again")
BT1.display(BT1.root,0)

print()
print("Are trees structurally the same: ",BT1.are_structurally_same_tree(BT.root, BT1.root))
print()

print()
print("Are trees mirror of each other: ",BT1.are_mirror_of_each_other(BT.root, BT1.root))
print()

print()
print("Is the true balanced: ", BT1.is_balanced(BT1.root))
print()

#DELETE TREE
print("#----------Deletion Methods--------------#")
print()
root = BT.delete_tree_iter(BT.root)
print("BT Tree deleted")
print()

root = BT1.delete_binary_tree_rec(BT1.root)
print("BT1 Tree deleted")
print()

"""
Output
#---------Create Tree instance----------#
#---------Add nodes to the tree----------#

    16

  15

    12

10

    6

  5

    4

#----------Traversal Methods----------------#

Only print extreme left nodes in reverse
4 5 10 None


Only print extreme left starting from root
10 5 4 None


Only print extreme right in reverse
16 15 10 None


All left nodes
10 5 4 12 None


All right nodes
10 6 15 16 None

PreOrder Traversal (recur) -->10 5 4 6 15 12 16 
PreOrder Traversal (iter) -->10 5 4 6 15 12 16 

InOrder Traversal (recur) -->4 5 6 10 12 15 16 
InOrder Traversal (iter) -->4 5 6 10 12 15 16 
Kth node in InOrder Traversal (iter) -->4 

PostOrder Traversal (recur) -->4 6 5 12 16 15 10 


LevelOrder Traversal -->10 5 15 4 6 12 16 

LevelOrder Traversal line by line
10 
5 15 
4 6 12 16 

Reverse LevelOrder Traversal
16 12 6 4 15 5 10 

Print all ancestors of a node
15,10,
Print nodes in a spiral order
10 5 15 16 12 6 4 
Lowest common ancestor of two nodes
None

Root to Leaf paths
[10, 5, 4]
[10, 5, 6]
[10, 15, 12]
[10, 15, 16]


#----------Aggregated Methods--------------#
Max elem in the BT (recur) is 16
Max elem in the BT(iter) is 16

Height of the BT(recur) is  3
Height of the BT(iter) is  3

Deepest node of the tree iter is 16

Search->Item 5 found in the tree
Search->Item 10 found in the tree Iter

Sum of all elems (recur) is  68
Sum of all elems (iter) is  68

Sum of all left leaves (recur) is  16

Diameter of the tree is  5

Sum at level 1 is->10
Sum at level 2 is->20
Sum at level 3 is->38

Sum at  1 is->10
Sum at  2 is->20
Sum at  3 is->38
Level with max sum  3

Sum at each level :  1 10
Average at level : 1 10.0
Sum at each level :  2 20
Average at level : 2 10.0
Sum at each level :  4 38
Average at level : 4 9.5

Vertical sum for each column is : 
{-2: 4, -1: 5, 0: 28, 1: 15, 2: 16}

#----------Node Count Methods--------------#
total nodes of the BT (recur) is 7
total nodes of the BT (iter) is 7

Num of full nodes  3
Num of full nodes (recur):  3

Num of half nodes  0
Num of half nodes (recur):  0

Num of leaf nodes  4
Num of leaf nodes (recur)  4

Node Count at level  1 is->1
Node Count at level  2 is->2
Node Count at level  3 is->4
#----------View Methods--------------#
Bottom View of the tree is 
{0: 12, -1: 5, 1: 15, -2: 4, 2: 16}

Top View of the tree is 
{0: 10, -1: 5, 1: 15, -2: 4, 2: 16}

Right View of the binary Tree is :
10 15 16 
10 15 16 

Left View of the tree (recur) is:
10 5 4 
Left view iterative of the tree is: 
10 5 4 

#---------Remove node 4 from the tree------#

    16

  15

    12

10

    6

  5

#----------Construction Methods--------------#

Construct BT from inorder and pre-order sequence in a list

    70

  60

    55

50

    45

  40

      35

    30

      20
Construct BT from level order and inorder sequence in a list

  22

20

      14

    12

      10

  8

    4

Convert BT tree to its mirror

  5

    6

10

    12

  15

    16

#----------Create another Tree-------------#

    16

  15

    12

10

    6

  5

    4

Node 4 removed which had no children. Display Tree again

    16

  15

    12

10

    6

  5


Node 15 removed which had two rows. Display Tree again

  16

    12

10

    6

  5

Are trees structurally the same:  True


Are trees mirror of each other:  False


Is the true balanced:  True

#----------Deletion Methods--------------#

BT Tree deleted

BT1 Tree deleted
"""