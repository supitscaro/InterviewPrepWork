### Mutable data types
- list
- dictionary
- set
- use-defined classes

### Immutable data types
- int
- float
- decimal
- bool
- string
- tuple
- range

### Primitive Types
- integer
- string
- boolean
- float

### Sets
- sets are unordered
- every element is unique, no duplicates are allowed
- a set may be modified, but the elements in the set must be immutable type

- you can create a set using the built-in set() function
    - the argument that goes inside is an iterable like a list or tuple or string.
- you can also use curly brace {} to create a set
    - this won't have key-value sets. the format will be similar to a list
    - set expects just one argument

:bangbang: when sets are defined with the curly braces, each element becomes a distinct element of the set, even if iterable.

```python
set_one = {'foo', 'bar', 'foo'}
print(set_one) # {'foo', 'bar'}

set_two = set('test')
print(set_two) # {'t', 's', 'e'}
```

#### Unions of Sets
- this returns both sets combined

```python
set1 = {'foo', 'bar', 'test'}
set2 = {'axs', 'ppl', 'txt'}
```
- the union of set1 and set 2 is: `{'foo', 'bar', 'test', 'axs', 'ppl', 'txt'}`

- a set union can be done with the | operator.

```python
set1 | set2
# {'foo', 'bar', 'test', 'axs', 'ppl', 'txt'}
```
:bangbang: you can use the .union() method to create a union as well, BUT the operator and method have a small difference between them.
    - when using the | operator, BOTH operands have to be sets.
    - the .union() method will take any other iterable as an argument, convert it to a set, then do the union.

#### Intersection of Sets
- this returns the common elements between both sets

- you can do this in two ways, using the & operator or the .intersection() method.

```python
a = {1, 2, 3, 4}
b = {4, 5, 7, 7}
c = {4, 5, 9, 6}

a.intersection(b, c) # {4}
a & b & c # {4}
```

#### Difference of Sets
- returns the set of all elements that are in one set but not the other

- you can do this in two ways, using .difference() method or - operator.

```python
a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

a.difference(b, c) # {1, 2, 3}

a - b - c # {1, 2, 3}
```

### Lists
- a collection of arbitrary objects, similar to an array

#### important notes
- lists are ordered
- lists can contain any arbitrary objects
- list elements can be accessed by index
- lists can be nested to arbitrary depth
- lists are mutable
- lists are dynamic

- Lists are mutable
- Methods that modify a list:
    - .append()
    - .extend()
    - .insert()
    - .remove()
    - .pop()


### Dictionaries
-
