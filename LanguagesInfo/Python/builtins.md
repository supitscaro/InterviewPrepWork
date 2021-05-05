### Filter
- this function takes two arguments:
    - function: can be a predefined function; most of the times it's a lambda function
    - iterable: an iterable object such as a list, tuple, dict

#### using a lambda function
```python

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
