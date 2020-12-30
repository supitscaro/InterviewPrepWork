# Big O

[Big O Measuring Performance](https://www.geeksforgeeks.org/understanding-time-complexity-simple-examples/ "Big O Measuring Performance")

## Measuring Performance (Time Complexity)
- **O(n^2)**: You ask the first person of the class if they have the pen, then you ask this person about the other 99 people in the classroom if they have that pen.

- **O(n)**: Going and asking each student individually.

- **O(log n)**: I divide the class into two groups. I ask if the pen is on the left or the right side of the classroom. Then I take that group and divide that group into two and ask again, and so on until I'm left with one person who has the pen.

## Deriving Big O (Asymptotic Analysis)
1. Define the function
    - count the number of expression executions

![Big O](/Users/carolinemendez/Desktop/InterviewPrep/images/bigOAcademind.png)

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

## Hash Tables

### What is a Hash Table?
- A hash table is a data structure that provides a mapping from keys to values
using a technique called hashing.
- We refer to these as key-value pairs.
- Keys must be unique, but values can be repeated.
- The key-value pairs you can place in a hash table can be of any type not just strings and numbers, but also objects! However, the keys need to be hashable.

- A hash function H(x) is a function that maps a key 'x' to a whole number in a fixed range.

- We can also define hash functions for arbitrary objects such as strings, lists, tuples, multi data objects, etc...

### Properties of Hash functions
- a hash function H(x) must be deterministic
- This means that if H(x) = y then H(x) must always produce y and never another value. This may seem obvious, but it is critical to the functionality of a hash function.

- We try very hard to make uniform hash functions to minimize the number of hash collisions.
- A hash collision is when two objects x, y hash to the same value (i.e. H(x) = H(y)).

### How does a hash table work?
- Ideally we would like to have a very fast insertion, lookup and removal time for the data we are placing within our hash table.
- Remarkably, we can achieve all this in O(1)* time using a hash function as a way to index into a hash table
- *This constant time behavior attributed to hash tables is only true if you have a good uniform hash function

### Dealing with Hash Collisions
- **Separate Chaining** deals with hash collisions by maintaining a data structure (usually a linked list) to hold all the different values which hashed to a particular value.

- **Open Addressing** deals with hash collisions by finding another place within the hash table for the object to go by offsetting it from the position to which it hashed to

### Time Complexity
- Insertion: **AVG** - O(1) **WORST** O(n)
- Removal: **AVG** - O(1) **WORST** O(n)
- Search: **AVG** - O(1) **WORST** O(n)
*The constant time behavior attributed to hash tables is only true if you have a good uniform hash function*

### What is Separate Chaining?
- Separate chaining is one of many strategies to deal with hash collisions by maintaining a data structure (usually a linked list) to hold all different values which hashed to a particular value.

### How to maintain O(1) insertion and lookup time complexity once my hash table gets really full and have long linked list chains?
- Once the hash table contains a lot of elements you should create a new hash table with a larger capacity and rehash all the items inside the old hash table and disperse them throughout the new hash table at different locations.

### How do I remove key-value pairs from my hash table?
- Apply the same procedure as doing a lookup for a key, but this time instead of returning the value associated with the key remove the node in the linked list data structure.

### Can I use another data structure to model the bucket behavior required for the separate chaining method?
- Of course, common data structures used instead of a linked list include: arrays, binary trees, self-balancing trees, etc. You can even go with a hybrid approach like Java's HashMap. However, note that some of these are much more memory intensive and complex to implement than a simple linked list which is why they may be less popular.
