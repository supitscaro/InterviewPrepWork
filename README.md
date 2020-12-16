# Data Structures

## Arrays

### What is a static array?
- a fixed length container containing n elements indexable from the range [0, n - 1].

### What is meant by being indexable?
- this means that each slot/index in the array can be referenced with a number.

### When and where is a static array used?
- storing and accessing sequential data.
- temporarily storing objects
- used by IO routines as buffers
- Lookup tables and inverse lookup tables.
- Can be used to return to multiple values from a function.
- Used in dynamic programming to cache answers to subproblems.

### Complexity for Static Array:
- Access: O(1) ... because of the property that arrays are indexable
- Search: O(n) ... could take linear time bc we potentially have to traverse all elements
- Insertion: N/A ... doesn't make sense from static array POV
- Appending: N/A
- Deletion: N/A

### Complexity for Dynamic Array:
- Access: O(1) ... because of the property that arrays are indexable
- Search: O(n) ... could take linear time bc we potentially have to traverse all elements
- Insertion: O(n) ... you could potentially have to shift all elements to right and recopy elements
- Appending: O(1) ... when we append elements, we have to resize the internal static array containing all elements, but happens so rarely
- Deletion: O(n) ... you could have to shift all elements over and potentially recopy all elements


## Dynamic Array
## How can we implement a dynamic array?
- One way is to use a static array!
1. Create a static array with an initial capacity.
2. Add elements to the underlying static array, keeping track of the number of elements.
3. If adding another element will exceed the capacity, then create a new static array with
    twice the capacity and copy the original elements into it.

## Linked Lists

## What is a linked list?
- A linked list is a sequential list of nodes that hold data which point to other nodes also containing data.

## Where are linked lists used?
- Used in many List, Queue, & Stack implementations
- Great for creating circular lists.
- Can easily model real world objects such as trains.
- Used in separate chaining, which is present certain Hashtable implementations to deal with hashing collisions.
- Often used in the implementation of adjancency lists for graphs

## Terminology
- Head: the first node in a linked list
- Tail: the last node in a linked list
- Pointer: reference to another node
- Node: an object containing data and pointer(s)

### Singly Linked Lists
- Singly linked lists only hold a reference to the next node. In the implementation you always maintain a reference to the head to the linked list and a reference to the tail nose for quick additions/removals.

#### Pros
- Uses less memory
- Simpler implementation

#### Cons
- Cannot easily access previous elements

### Complexity
- Search: O(n) ... if the element is not there, we traverse all of the elements
- Insert at head: O(1) ... we always maintain a pointer to the head
- Insert at tail: O(n) ... we always maintain a pointer to the head
- Remove at head: O(1) ... we have a reference to it, so we can just remove it
- Remove at tail: O(n) ... even if we have a reference, we can only remove it once because we cant reset the value of what the tail is
- Remove in middle: O(n) ... in worst case, we would need to traverse through n - 1 elements which is linear

### Doubly Linked Lists
- With a doubly linked list each node holds a reference to the next and previous node. In the implementation you always maintain a reference to the head and the tail of the doubly linked list to do quick additions/removals from both ends of your list.

#### Pros
- Can be traversed backwards

#### Cons
- Takes 2x memory

### Complexity
- Search: O(n) ... if the element is not there, we traverse all of the elements
- Insert at head: O(1) ... we always maintain a pointer to the head
- Insert at tail: O(n) ... we always maintain a pointer to the head
- Remove at head: O(1) ... we have a reference to it, so we can just remove it
- Remove at tail: O(1) ... we have a pointer to the previous node
- Remove in middle: O(n) ... in worst case, we would need to traverse through n - 1 elements which is linear
