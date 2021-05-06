### Filter
- this function takes two arguments:
    - function: can be a predefined function; most of the times it's a lambda function
    - iterable: an iterable object such as a list, tuple, dict

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
