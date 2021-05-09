### Filter
- this function takes two arguments:
    - function: can be a predefined function; most of the times it's a lambda function
    - iterable: an iterable object such as a list, tuple, dict
- the function passed in will return a boolean
- filter() will return a new iterable with each item from the iterable

#### using a lambda function
```python
num_list = [10, 20, 18, 4, 20]

res = list(filter(lambda n: x * 10, num_list)) # returns elements multiplied by 10
print(res)
```

#### using predefined function
```python
def multiply_by_10(n):
    return n * 10

num_list = [10, 20, 18, 4, 20]

res = list(filter(multiply_by_10, num_list))
print(res)
```

### Map
- applies a function to all items in a list
- will return a new iterable that contains each item returned from the function parameter
- the return value can be passed to list(), set(), etc to return that specific type

#### without map function
```python
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

#### with map function
```python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
```

### Sorted
- with no additional arguments or parameters, sorted() orders the values in an ascending order
- the original variable is unchanged. sorted() provides sorted output and does not change the original value in place
- when called, it provides an ordered list as a return value

#### Key argument
- this argument expects a function to be passed to it and that function will be used on each value in the list being sorted to determine the resulting order

- sorted() example: sorted(iterable, key=None, reverse=False)
    - the extra parameters must be set using the name and equal sign

### Enumerate
- takes two parameters:
    - iterable: anything that supports iteration
    - start (optional): starts counting from this number. if omitted, 0 is taken as start

- these enumerate objects can be converted to list and tuples

```python
grocery = ['bread', 'milk', 'butter']
enumerated_grocery = enumerate(grocery)

print(list(enumerated_grocery))
# [(0, 'bread'), (1, 'milk'), (2, 'butter')]
```
### Any
- takes an iterable such as a list, string, dictionary
- returns a boolean value
- returns True if at least one element of an iterable is true
- returns False if all elements are false or if an iterable is empty

- when it comes to dictionaries, if all keys are not false or the dictionary is empty, any() returns False.
- if at least one key is true, any() returns True

- all values are true => returns true
- all values are false => returns false
- one value is true => returns true
- one value is false => returns true
- empty iterable => returns false

```python
# returns True because 1, 3, and 2 is true
lst = [1, 3, 2, 0]
print(any(lst))

# returns False because both are Falsy values
lst2 = [0, None]
print(any(lst2))

# returns True since 9 is true
lst3 = [0, False, 9]
print(any(lst3))

# all elements are true so it returns true
string = "This is a test"
print(any(string))

# returns True because a string of 0 is true
string2 = "0"
print(any(string2))

# returns False because None is falsy
string3 = "None"
print(any(string3))

# returns false because the empty string is false
string4 = ""
print(any(string4))

# returns False because 0 is None
d = {0: 'None'}
print(any(d))

# returns true because 1 is True
d2 = {1: 'True', 2: 'False'}
print(any(d2))

# returns false because it's an empty dict
d3 = {}
print(any(d3))
```
### All
- takes an iterable such as list, tuple, dictionary
- returns true if *all* elements are true
- returns false if *any* elements are false

- all values are true => return is true
- all values are false => return is false
- one value is true => return is false
- one value is false => return is false
- empty iterable => true
    - the reason an empty iterable returns true is because there are no values that DON'T satisfy the condition, so all() returns a true value

- when it comes to dictionaries, if all keys are true, all() returns true.

```python
# returns false because one value is false (0)
lst = [1, 2, 3, 0]
print(all(lst))

# returns true because there are no values that don't satisfy the condition
lst2 = []
print(all(lst2))

# returns true
string = "This works"
print(all(string))

# returns true
string2 = "0"
print(all(string2))

# returns true
string3 = ""
print(all(string3))

# returns true
d = {'0': 'True'}
print(all(d))
```
