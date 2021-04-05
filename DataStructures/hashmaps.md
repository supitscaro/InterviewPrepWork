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
