## Linked Lists

### What is a linked list?
- A linked list is a sequential list of nodes that hold data which point to other nodes also containing data.

### Where are linked lists used?
- Used in many List, Queue, & Stack implementations
- Great for creating circular lists.
- Can easily model real world objects such as trains.
- Used in separate chaining, which is present certain Hashtable implementations to deal with hashing collisions.
- Often used in the implementation of adjancency lists for graphs

### Terminology
- Head: the first node in a linked list
- Tail: the last node in a linked list
- Pointer: reference to another node
- Node: an object containing data and pointer(s)

## Singly Linked Lists
- Singly linked lists only hold a reference to the next node. In the implementation you always maintain a reference to the head to the linked list and a reference to the tail nose for quick additions/removals.

![Compare Algorithms](images/linkedlist.png)

### Pros
- Uses less memory
- Simpler implementation

### Cons
- Cannot easily access previous elements

### Complexity
- Search: O(n) ... if the element is not there, we traverse all of the elements
- Insert at head: O(1) ... we always maintain a pointer to the head
- Insert at tail: O(n) ... we always maintain a pointer to the head
- Remove at head: O(1) ... we have a reference to it, so we can just remove it
- Remove at tail: O(n) ... even if we have a reference, we can only remove it once because we cant reset the value of what the tail is
- Remove in middle: O(n) ... in worst case, we would need to traverse through n - 1 elements which is linear

## Doubly Linked Lists
- With a doubly linked list each node holds a reference to the next and previous node. In the implementation you always maintain a reference to the head and the tail of the doubly linked list to do quick additions/removals from both ends of your list.

![Compare Algorithms](images/doublylinked.png)

### Pros
- Can be traversed backwards

### Cons
- Takes 2x memory

### Complexity
- Search: O(n) ... if the element is not there, we traverse all of the elements
- Insert at head: O(1) ... we always maintain a pointer to the head
- Insert at tail: O(n) ... we always maintain a pointer to the head
- Remove at head: O(1) ... we have a reference to it, so we can just remove it
- Remove at tail: O(1) ... we have a pointer to the previous node
- Remove in middle: O(n) ... in worst case, we would need to traverse through n - 1 elements which is linear
