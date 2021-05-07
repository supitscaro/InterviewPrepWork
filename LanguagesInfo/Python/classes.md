## OOP

### Classes
- classes define functions called methods, which identify behaviors and actions that an object created from the class can perform with its data

### __init__
- the ```__init__()``` sets the initial state of the object by assigning the values of the object's properties
    - this initializes each new instance of the class
- this can take any # of parameters, but the first one will always be **self**
- when a new class instance is created, the instance is automatically passed to the self parameter in the `__init__` so that new attributes can be defined on the object

#### __init__ attributes
- attributes created here are called instance attributes
- these attributes' values are specific to a particular instance of the class

#### class attributes
- these attributes have the same value for all class instances
- you define these by assigning a value to a variable name outside of `__init__`

### instantiate a class
- to instantiate a class, all you need to do is invoke the class with an opening and closing parenthesis

### instance methods
- functions that are defined inside of a class and can only be called from an instance of that class
- its first parameter is always self

### Getters
- a method that gets a value of a property but looks like a normal property
- this helps to access private attributes from a class

#### property decorator
- we can apply this to a method to make it more readable
- decorators allow us to change the way a method will get invoked


```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def desc(self):
        return f"{self.name} is {self.age} years old"


puppy = Dog()
print(puppy.desc) # versus doing puppy.desc()
```

### Setters
- this is a method that gets invoked with the assignment operator
- this actually sets the value of a property
- this helps set the value to private attributes in a class
