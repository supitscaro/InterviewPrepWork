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
