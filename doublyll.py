# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:29:03 2024

@author: Balaji
"""

#class node:
#    def __init__(self):
#        self.data = data
#        self.prev = None
#        self.next = None

#def froward_trev(head):
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def insertNode(list):
    
    head = None
    current = None
    
    for value in list:
        newnode = Node(value)
        if head is None:
            
            head = newnode
            print(head)
        else:
            current.next = newnode
            newnode.prev = current
        current = newnode
    print("Ss")
    return head


def traverse(head):
    if head is None:
        print("Empty")
        return 0
    current = head
    while current is not None:
        print(current.data)
        current = current.next


def deleteNode(head, delnum):
    current = head
    
    while current is not None:
        if current.data == delnum:
            
            if current.prev is None:
                head = current.next
            
                if head is None:
                    head.prev = None
                    
            elif current.next is None:
                current = None
                
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                
            return head
        
        current = current.next

        
def reversesDll(head):
    current = head
    newhead = None
    
    while current is not None:
    
        current.prev = current.next
        current.next = current.prev
        
        newhead = current
        current = current.prev  
        
    print(newhead)
    print(newhead.next)
    return newhead
       

def linkedlistcheckdiv(head, x):

    current = head
    while current is not None:
        if (current.data % x == 0):
            print(current.data)

        current = current.next
    return 0



arr = [10, 15, 20, 50]
head = insertNode(arr)
deleteNode(head, 15)
linkedlistcheckdiv(head, 10)
#print(head.next)
a = reversesDll(head)
#print(a)
traverse(a)          




    
    
    
    
    