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
```python
set1 = {'foo', 'bar', 'test'}
set2 = {'axs', 'ppl', 'txt'}
```
- the union of set1 and set 2 is:
```python
{'foo', 'bar', 'test', 'axs', 'ppl', 'txt'}`
``
