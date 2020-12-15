## What is a static array?
- a fixed length container containing n elements indexable from the range [0, n - 1].

## What is meant by being indexable?
- this means that each slot/index in the array can be referenced with a number.

When and where is a static array used?
- storing and accessing sequential data.
- temporarily storing objects
- used by IO routines as buffers
- Lookup tables and inverse lookup tables.
- Can be used to return to multiple values from a function.
- Used in dynamic programming to cache answers to subproblems.

Complexity for Static Array:
- Access: O(1) ... because of the property that arrays are indexable
- Search: O(n) ... could take linear time bc we potentially have to traverse all elements
- Insertion: N/A ... doesn't make sense from static array POV
- Appending: N/A
- Deletion: N/A

Complexity for Dynamic Array:
- Access: O(1) ... because of the property that arrays are indexable
- Search: O(n) ... could take linear time bc we potentially have to traverse all elements
- Insertion: O(n) ... you could potentially have to shift all elements to right and recopy elements
- Appending: O(1) ... when we append elements, we have to resize the internal static array containing all elements, but happens so rarely
- Deletion: O(n) ... you could have to shift all elements over and potentially recopy all elements


Dynamic Array
How can we implement a dynamic array?
- One way is to use a static array!
1. Create a static array with an initial capacity.
2. Add elements to the underlying static array, keeping track of the number of elements.
3. If adding another element will exceed the capacity, then create a new static array with
    twice the capacity and copy the original elements into it.
