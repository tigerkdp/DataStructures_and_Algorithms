#LinkedList - Singly.
#create node class
#create linked list class
#author: tigerkdp. 

class Node:
    
    def __init__(self, data):
        self.info = data
        self.link = None
        
class LinkedList:
    
    def __init__(self):
        self.start = None
        
    def print_list(self):
        
        if self.start is None:
            print("List is Empty")
            return
        
        l = self.start
        print("[", end="")
        while l is not None:
            print(l.info, end=", ")
            l = l.link
        print("]")
            
    #INSERT METHODS 
            
    def insert_at_begin(self,data):         #O(1)
        new_node = Node(data)
        
        if self.start is None:
            self.start = new_node
        else:
            new_node.link = self.start
            self.start = new_node

            
    def insert_at_end(self,data):          #O(N)
        new_node = Node(data)
        
        if self.start is None:
            self.start = new_node
        
        l = self.start
        while l.link is not None:
            l = l.link
        l.link = new_node
        
        
    def insert_before_x_value(self, data, x):
        new_node = Node(data)
        
        l = self.start
        while l.link is not None:
            if l.link.info == x:
                break
            else:
                l = l.link
        new_node.link = l.link
        l.link = new_node

    def insert_after_x_value(self, data, x):
        new_node = Node(data)
        
        l = self.start
        
        while l is not None:
            if l.info == x:
                break
            l = l.link
            
        new_node.link = l.link
        l.link = new_node  
        
    def insert_at_kth_pos(self, data, k):
        #list starts at 0th position
        new_node = Node(data)
        
        if k == 0:
            new_node.link = self.start
            self.start = new_node
            return
        
        kth = 1
        l = self.start        
        while kth < k and l is not None:
                l = l.link
                kth = kth+1
                
        new_node.link = l.link
        l.link = new_node

        
    #REMOVAL METHODS 
    
    def remove_from_begin(self):             #O(1)
        
        if self.start is None:
            return
        
        if self.start.link is None:
            self.start = None
        else:
            self.start = self.start.link
            
        
    def remove_from_end(self):                #O(N)
        
        if self.start is None:
            return
        
        if self.start.link is None:
            self.start = None
        else:
            l = self.start
            while l.link.link is not None:
                l = l.link
            l.link = None
         
    def remove_x_value(self, x):              #O(N)
        
        if self.start is None:
            return None    
        
        #first node
        if self.start.info == x:
            self.start = self.start.link
            return

        #other node
        l = self.start 
        while l.link is not None:
            if l.link.info == x:
                l.link = l.link.link
                return
            else:
                l = l.link
        print("Node not found")
                   
        
    def remove_from_kth_pos(self, k):               #O(N)
        #list starts at 0th position
        if self.start is None:
            return
        
        #first position
        if self.start.link is None:
            self.start = self.start.link
            return
        
        l = self.start
        count = 0
        prev = None
        while l is not None:           
            if count == k:
                break
            prev = l
            count +=1
            l=l.link
        
        prev.link = l.link
                
    def remove_nth_node_from_end(self, n):             #O(N) 
        fast = self.start
        slow = self.start
        nth = 0
        while nth != n:
            nth +=1
            fast = fast.link
           
        prev = self.start
        while fast is not None:
            prev = slow
            slow = slow.link
            fast = fast.link
        
        if prev == self.start:
            self.start = self.start.link
        else:
            prev.link = slow.link   
            
    #TRAVERSING METHODS       
            
    def traverse_recur_fwd(self, start):
        
        if start is None:
            return
        else:
            print(start.info, end=",")
            self.traverse_recur_fwd(start.link)
            
    def traverse_recur_bkwd(self, start):
        
        if start is None:
            return
        else:
            self.traverse_recur_bkwd(start.link) 
            print(start.info, end=",")  
            
            
    def traverse_recur_fwd_back(self, start):
        
        if start is None:
            return
        print(start.info, end=",")
        if start.link is not None:
            self.traverse_recur_fwd_back(start.link.link)
        print(start.info, end=",")
        
    def traverse_recur_alt(self, start, count):
        
        if start is None:
            return
        else:
            if count % 2 == 0:
                 print(start.info, end=",") 
            self.traverse_recur_alt(start.link, count+1) 
            if count % 2 != 0:
                print(start.info, end=",")  
    
    #AGGREGATE METHODS (COUNT, SUM, MAX, MIN, AVG)
    
    def list_size(self):                              #O(N)
        size = 0
        
        if self.start is None:
            return 0
        
        l = self.start
        while l.link is not None:
            size +=1 
            l = l.link
            
        #test 
        print("list size :", size)
        return size
        
    
    def sum_of_elem(self):                           #O(N)
         
        if self.start is None:
            return
        
        l = self.start
        sum1 = 0
        while l is not None:
            if type(l.info) != str:
                sum1 = sum1+l.info
            else:
                pass
            l = l.link
            
        #test
        print("Sum of numerical values is ", sum1)
        
        return sum1
    

    def max_of_elem(self):                            #O(N)
        
        if self.start is None:
            return
        
        l = self.start
        max1 = float("-inf")
        while l is not None:
            if type(l.info) != str:
                if l.info > max1:
                    max1 = l.info
            else:
                pass
            l = l.link
            
        #test
        print("Max of numerical values is ", max1)
        
        return max1
    
    
    def min_of_elem(self):                            #O(N)
        
        if self.start is None:
            return
        
        l = self.start
        min1 = float("inf")
        while l is not None:
            if type(l.info) != str:
                if l.info < min1:
                    min1 = l.info
            else:
                pass
            l = l.link
            
        #test
        print("Min of numerical values is ", min1)
        
        return min   
    
    
    def ave_of_num_elem(self):                         #O(N)
        
        avg = self.sum_of_elem()/self.list_size()
        print("Aver of numerical values is ", round(avg,2))
        return avg
    
        
    #GET METHODS
    
    def search_element_k(self, k):                    #O(N)
        l = self.start
        
        node_pos = 0  #pos starts at 0 in the list
        while l is not None:
            if l.info == k:
                print("{} found at pos {}.".format(k, node_pos))
                return node_pos
            else:
                node_pos +=1
                l = l.link
        return None
    
    def get_nth_Node(self, n):                       #O(N)
        l = self.start
        nth = 0
        while n != nth:
            l = l.link
            nth +=1
        print("Node value {} from {} pos".format(l.info, n))
        return l.info
    
    def get_nth_node_from_end(self, n):                  #O(N)
        fast = self.start
        slow = self.start
        nth = 0
        while nth != n:
            nth +=1
            fast = fast.link
            
        while fast is not None:
            slow = slow.link
            fast = fast.link
        
        #test print
        print("{}th node from end contains {}".format(n, slow.info))
        return slow.info

    def get_first_node(self):                       #O(1)
        
        if self.start is None:
            return
        else:
            #test print
            print("first node contains  ", self.start.info)
            return self.start.info

    def get_last_node(self):                        #O(N)
        
        if self.start is None:
            return
        
        l = self.start
        while l.link is not None:
            l = l.link    
        #test print
        print("last node contains ", l.info)
        return l.info
    
    def get_middle_node(self):                        #O(N)
        
        if self.start is None:
            return
        
        slow = self.start
        fast = self.start
        
        while fast is not None and fast.link is not None:
            slow = slow.link
            fast = fast.link.link
        
        #test print
        print("middle node contains", slow.info)
        return slow.info        
    
    #REVERSE LIST METHODS
    
    def reverse_list_iterative(self):              #O(N)
        
        if self.start is None:
            return
        
        prev= None
        next1 = None
        
        l = self.start
        while l is not None:
            next1 = l.link
            l.link = prev
            prev  =  l
            l = next1
        self.start = prev
        
        #test
        self.print_list()
        return 
    
    def reverse_list_using_stack(self):                #O(N),  space: O(N)

        stack = []
        l  = self.start
        while l is not None:
            stack.append(l)
            l = l.link
        
        while stack:
            self.remove_from_begin()
            popped = stack.pop()
            self.insert_at_end(popped.info)
        
        #test
        self.print_list()
        
        return
    
    def reverse_list_recursive(self, start):
        
        if start.link is None:
            self.start = start
            return start
        else:
            self.reverse_list_recursive(start.link)
            temp = start.link
            temp.link = start
            start.link = None
            
    def reverse_sublist_iter(self, m, n):
        if m == n:
            return
        
        dummy = Node(0)
        dummy.link = self.start
    
        p, prev = self.start, dummy
        
        for i in range(m - 1):
            p = p.link
            prev = prev.link
        
        for i in range(n-m):
            next1 = p.link
            p.link = next1.link
            next1.link = prev.link
            prev.link = next1
    
        return self.start
    
    def reverse_sublist_ingroup(self, start, k):
        
        p = start
        next1 = None
        prev = None
        count =0
        
        while p is not None and count < k:
            next1 = p.link
            p.link = prev
            prev = p
            p = next1
            count += 1
        
        if p is not None:
            start.link = self.reverse_sublist_ingroup(p, k)
    
        return prev
    #SWAPPING Methods
    
    def pairwise_swap_iterative(self):
        
        if self.start is None:
            return
        
        l = self.start        
        while l is not None and l.link is not None:
            l.info, l.link.info = l.link.info, l.info
            l = l.link.link
            
    #LOOP/CYLE RELATED METHODS

    def add_loop_at_index_k(self, k):
        #k is the index from the start (not end)
        
        if self.start is None:
            return
        
        prev = self.start
        l = self.start
        count = 0

        while l.link is not None:
            if count != k:
                count +=1
                prev = l

            l=l.link
        
        if count == k:
            l.link = prev
            return True
        else:
            return False
        
        
    def add_loop_at_node_containing_k(self, k):
        
        if self.start is None:
            return
        
        prev = self.start
        l = self.start
        value_found = 0
        
        while l.link is not None:
            if l.info == k:
                prev = l
                value_found = 1
            l = l.link
            
        if value_found == 1:
            l.link = prev
            return True
        else:
            return False
    
    def detect_loop(self):
        if self.start is None:
            return
        
        slow = self.start
        fast = self.start
        
        while fast.link is not None:
            slow = slow.link
            fast = fast.link.link
            
            if slow == fast:
                return slow
        return False   
    
    def loop_length(self):
        
        if self.start is None:
            return
        
        loop = self.detect_loop()
        if loop is None:
            return
        
        #find loop
        p = loop
        q = loop
        len_cycle = 0
        while True:
            len_cycle+=1
            q = q.link
            
            if q == p :
                break
        return len_cycle

    
    def remaining_list_length(self):
        
        if self.start is None:
            return
        
        loop = self.detect_loop()
        if loop is None:
            return
    
        #find loop
        p = loop
        q = loop
          #find remaining list length
        len_remaining_list = 0
        
        p = self.start
        while p != q:
            len_remaining_list+=1
            p = p.link
            q = q.link
        return len_remaining_list
    

    def detect_loop_node(self):
        
        if self.start is None:
            return
        
        len_cycle = self.loop_length()
        print("Length of the loop is ", len_cycle)
        
        len_remaining_list = self.remaining_list_length()
        print("Len of rem list ", len_remaining_list)
        
        l = self.start
        for i in range(len_remaining_list):
            l = l.link
        print("Loop begins at node containing", l.info)
    
    
    def remove_cycle(self):
        
        if self.start is None:
            return
        
        len_cycle = self.loop_length()
        len_remaining_list = self.remaining_list_length()
      
        total_list_length = len_cycle + len_remaining_list
        
        
        # start from beginning till list length
        l = self.start
        for i in range(total_list_length-1):
            l = l.link
        l.link = None   
        
        print("Total List length ", total_list_length)
        print("Cycle Removed")
        
        

    
    #DUPLICATE METHODS
    
    def remove_dup_nodes_unsorted(self):           #O(N) space:O(N)
        
        ht = []       
        l = self.start
        ht.append(l.info)
        
        while l.link is not None:
            if l.link.info not in ht:
                ht.append(l.link.info)
                l = l.link
            else:
                l.link = l.link.link        
    
    
    def remove_dups_from_sorted(self):
        
        l = self.start
        while l.link is not None:
                if l.info == l.link.info:
                    l.link = l.link.link
                else:                   
                    l = l.link        

    def test_remove_dups_from_sorted(self):
        # this method is only created to test remove_dups_from_sorted method
        
        #clear original list. 
        self.start = None
        
        #insert items in list so it is a palindrom
        self.insert_at_begin(1)
        self.insert_at_begin(2)
        self.insert_at_begin(3)
        self.insert_at_begin(4)
        self.insert_at_begin(4)
        self.insert_at_begin(5) 
        
        self.print_list()
        self.remove_dups_from_sorted()
        self.print_list()
        
    #VALIDATION METHODS
        
    def is_list_lengh_even_or_odd(self):                 #O(N)
        #without using the count variable
        l = self.start
        
        while l is not None and l.link is not None:
            l = l.link.link
        if l is None:
            print("list is Even")
            return "Even"
        else:
            print("list is odd")
            return "Odd"
    
    
    def is_list_palindrome(self):                #O(N), space:O(N)
        st = []
        l = self.start

        while l is not None:
            st.append(l.info)
            l = l.link

        l = self.start

        while l is not None:
            temp = st.pop()
            if l.info == temp:
                l = l.link
            else:
                return "not a palindrome"
        return "Palindome"
    
    def test_palindrome(self):
        # this method is only created to test is_list_palindrome() method
        
        #clear original list. 
        self.start = None
        
        #insert items in list so it is a palindrom
        self.insert_at_begin('n')
        self.insert_at_begin('a')
        self.insert_at_begin('y')
        self.insert_at_begin('a')
        self.insert_at_begin('n')  #change this to k to test not
        
        pal_check = self.is_list_palindrome()
        print("list is", pal_check)
        
        
    # Merging two sorted list
    # Merging creating a new list
    # Merging by rearranging links

    # Merging by creating new list.  Size of both lists can be diff
    # Define P1 and P2.  Compare both.  Add smaller one to new list pM. pM is maintained at the end
    
    # Original list do not change
    def merge(self, p1, p2):
        
        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link
            
        pM = startM
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
                
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            
        return startM
    
    #Merge by rearranging links. 
    def merge_rearrage(self, p1, p2):
        
        if p1.info < p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link
            
        pM = startM
        
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link
                
        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1
            
        return startM
        

#test

L = LinkedList()

# INSERT METHODS Testing

print("#--------Insert Methods-----#")
#-----beginning------#
L.insert_at_begin(10)
L.insert_at_begin(10)
L.insert_at_begin(9)
L.insert_at_begin(8)

#------end--------#
L.insert_at_end(11)
L.insert_at_end(12)
L.insert_at_end('a')
L.insert_at_end("item1")
L.insert_at_end(3.4)

#-----before/after/kth----#
L.insert_before_x_value(9.5, 10)
L.insert_after_x_value(10.5, 10)
L.insert_at_kth_pos('po', 1)

L.print_list()
#[8, po, 9, 9.5, 10, 10.5, 11, 12, a, item1, 3.4, ]

#REMOVE Methods testing

#------begin/end/value---#
print("\n#---------Remove Methods-------#")
L.remove_from_begin()
L.remove_from_end()
L.remove_x_value(12)
L.print_list()
#[po, 9, 9.5, 10, 10.5, 11, a, item1, ]

#------from kth--------#
L.remove_from_kth_pos(4)
L.print_list()
#[po, 9, 9.5, 10, 11, a, item1, ]

#------from end--------#
L.remove_nth_node_from_end(7)
L.print_list()
#[9, 9.5, 10, 11, a, item1, ]


#TRAVERSE LIST RECURSIVELY
print("\n#-----Traverse recursively----#")
L.traverse_recur_fwd(L.start)
print()
L.traverse_recur_bkwd(L.start)
print()
L.traverse_recur_fwd_back(L.start)
print()
L.traverse_recur_alt(L.start,0)
print()

#AGGREGATED METHODS
print("\n#--------Aggregated methods---#")
L.list_size()
L.sum_of_elem()  #39.5
L.max_of_elem()  #11
L.min_of_elem()  #9
L.ave_of_num_elem() #6.58 (size includes str values)

#GET METHODS 
print("\n#-------Get Methods-------#")
L.search_element_k(11) #11 found at 3
L.get_nth_Node(2)
L.get_nth_node_from_end(2)
L.get_first_node()
L.get_last_node()
L.get_middle_node()


# REVERSE METHODS
print("\n#------reverse_methods-----#")
L.reverse_list_iterative()
L.reverse_list_using_stack()
L.reverse_list_recursive(L.start)
L.print_list()
L.reverse_sublist_iter(3,5)
L.print_list()
L.start = L.reverse_sublist_ingroup(L.start, 3)
L.print_list()

#SWAPPING_METHODS
print("\n#------swapping methods-----#")
L.pairwise_swap_iterative()
L.print_list()

#LOOP/CYCLE METHODS

print("\n#---cycle methods, add at index---#")
loop_added = L.add_loop_at_index_k(4)
if loop_added == True:
    L.detect_loop()
    L.detect_loop_node()
    L.remove_cycle()
else:
    print("Index not found. Loop not added")

print("\n#---cycle methods, add at node value---#")
loop_added = L.add_loop_at_node_containing_k(10)
if loop_added == True:
    L.detect_loop()
    L.detect_loop_node()
    L.remove_cycle()
else:
    print("Value not found. Loop not added")


print("\n#------Remove Duplicate methods-------#")
print("Dups from Unsorted list")      
L.print_list()
L.remove_dup_nodes_unsorted()
L.print_list()

print()
print("Dups from sorted list")
L.test_remove_dups_from_sorted()


#VALIDATION METHODS 
print("\n#-------Validation Methods-------#")
L.is_list_lengh_even_or_odd()
L.test_palindrome()  #new data is inserted to test this.

""" 
#----output-------#

#--------Insert Methods-----#
[8, po, 9, 9.5, 10, 10.5, 10, 11, 12, a, item1, 3.4, ]

#---------Remove Methods-------#
[po, 9, 9.5, 10, 10.5, 10, 11, a, item1, ]
[po, 9, 9.5, 10, 10, 11, a, item1, ]
[9, 9.5, 10, 10, 11, a, item1, ]

#-----Traverse recursively----#
9,9.5,10,10,11,a,item1,
item1,a,11,10,10,9.5,9,
9,10,11,item1,item1,11,10,9,
9,10,11,item1,a,10,9.5,

#--------Aggregated methods---#
list size : 6
Sum of numerical values is  49.5
Max of numerical values is  11
Min of numerical values is  9
Sum of numerical values is  49.5
list size : 6
Aver of numerical values is  8.25

#-------Get Methods-------#
11 found at pos 4.
Node value 10 from 2 pos
2th node from end contains a
first node contains   9
last node contains  item1
middle node contains 10

#------reverse_methods-----#
[item1, a, 11, 10, 10, 9.5, 9, ]
[9, 9.5, 10, 10, 11, a, item1, ]
[item1, a, 11, 10, 10, 9.5, 9, ]
[item1, a, 10, 10, 11, 9.5, 9, ]
[10, a, item1, 9.5, 11, 10, 9, ]

#------swapping methods-----#
[a, 10, 9.5, item1, 10, 11, 9, ]

#---cycle methods, add at index---#
Length of the loop is  4
Len of rem list  3
Loop begins at node containing item1
Total List length  7
Cycle Removed

#---cycle methods, add at node value---#
Length of the loop is  3
Len of rem list  4
Loop begins at node containing 10
Total List length  7
Cycle Removed

#------Remove Duplicate methods-------#
Dups from Unsorted list
[a, 10, 9.5, item1, 10, 11, 9, ]
[a, 10, 9.5, item1, 11, 9, ]

Dups from sorted list
[5, 4, 4, 3, 2, 1, ]
[5, 4, 3, 2, 1, ]

#-------Validation Methods-------#
list is odd
list is Palindome

"""