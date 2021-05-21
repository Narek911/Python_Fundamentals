"""
In Python everything is an object
#   Python data Types
    int
    float
    bool
    string is immutable

#   Python Data Structures (it is not possible to access the index that is don't declared)
    set unordered collection of unique items {} immutable
    list []
    tuple is immutable ()
    dictionary {'key': value}

#   Python Custom Data Type
    class

#   Python special Data Types
    external modules
    external packages

#   Other data types
    None
    complex

#   Python iterables
    list
    set
    tuple
    dictionary
    string

#   Python operators
    ** squires
    // Returns the int part

#   Python special
    *var -> list unpacking operator
    var = 100 / 5
    100 / 5 -> expiration (produces or executes)
    var = 100 / 5 -> statement
    f'{var}' -> formatted string
    r"()" -> row string
    slice[start, stop, step] it create a copy of the object
    [[]] -> the way to declare 2d list
    ternary operator if condition else
    is operator is checking the equality ov data types not data structures
    range(start, stop, step)
    enumerate(iterable, start=0) returns index and element of iterable object
    pass keyword force the interpreter to step to the next line
    Walrus operator := lets to assign value before conditional operators


#   Python functions
    In Python the function always returns something
    In case of function definition called parameters
    In case of function call called arguments
    function parameters can have default value assigned to them
    function arguments can be positional and keyword types
    in case when they are declared es keyword arguments they can be used without keeping the actual order

    docstring is the way to provide information about function
    can be called via help() function or can be printed via .__doc__ method

    *args are any number of positional arguments. In function they are represented as a tuple
    method to use in function call is following fun(1, 2, 3, 4, 5)
    **kwargs are any number of keyword arguments. In  function they are represented as dictionary
    method to use in function call is following fun(item1=1, item2=2, item3=3).
    to unpack kwargs use *kwargs.values()

    There is a order for parameters: params, *args, default parameter, **keyword argument

#   Scope rules
    1 -start with local scope
    2 -Parent local scope
    3 -Global (indentation is nothing)
    4 -build-in python function and variables

# Dependency resolution
    1   global keyword
        global var_name
        var_name += 1
    used as extern keyword in c. to have access global variables from function
    2   passing as parameters to the function
    3   nonlocal keyword intended modify parent local variable from local scope of inner define function

#   Python OOP
    class name should be upper case
    class BigObject: #class
        pass
    obj = BigObject() #instanciate
    obj #insteance
    print(type(obj))
    class has class object attributes which is static
    OOP let us to have memory effective, reliable, modular code

#   Method types are the followings:
    1 instance method: this should contain self parameter. It is the basic method type. It do not need decorator
    2 static method: This should be declared with @staticmethod decorator. it do not have access to the instance data
    It cant modify the instance data. it do not receive the any parameters.
    class method: THis should be declared with @classmethod decorator. it have limited access to the instance methods
    and can have access to the staticmethod. It need cls parameter which passed automatically by Python. we can use
    this method without instantiating the class

#   Property types are:
    Class Object property: defined outside of constructor and methods and visible in the class
    class own properties: can be accessed only via self


#   decorators are supper functions that can be created by us (custom decorators). It is wrap another function and
    changes it enhance  it. As soon as interpreter reaches @ keyword it refer to it as decorator
    def my_decorator(func):
        def wrap_func(*args, **kwargs):
            print('************')
            func(*args, **kwargs)
            print('************')
        return wrap_func

# There are 4 main pillars in OOP That it should support very well
#   Encapsulation It is binding the data and methods to the object
    If class only contains properties it is more effective to use dictionary instead
    Encapsulation encapsulates the functionality of the object
    It let us to use the methods of the other objects that we do not declare
#   Abstraction this is intended to hiding or abstracting information and giving access only
    the thing that are necessary. absolutely know what is underneath and how is the method is
    realised. you only use it. We only need to know how to use it.
    Abstraction is using public and private methods to hiding or allowing to used the certain functionality
    Python don't support private variables (methods and properties).
    there is only convention to declare with '_' or '__' underscore. If you see underscore please don't touch this
#   Inheritance allows to inherit methods or properties
    You should pass parent class to the inherited class as parameter like class Child(Parent):
    It allows us to abstracting the part of code that the inheritance class are shared
    The Inheritance has parent class and children class (subclasses or derived class)
    In python everything is inherited from the base class which is called 'object'
#   Polymorphism stands as poly -> many, morph -> form (many forms)
    Its refers to the way that classes can share the same method name, but the method reacts as needed for the
    particular class or object need
    It is possible to call the parent method from the child class using parent.method(self) syntax

#   super is used to automatically pass self to the parent constructor

#   Introspection is ability to determine the type of object at runtime
    dir() lets you to determine the list of supported properties and methods in python

#   Dunder methods They are magic methods in python. They are inherited from the base class 'object'
    Dunder methods are spacial type of method that allows as to use in build functions
    It is possible to modify dunder methods. dunder method referenced to the build-in function so the
    changes that have benn made on the dunder method affects on the build-in function. They are allows to
    overwrite the build-in functions for the specified object or class

#   The Object which is instance of the class has only the methods and properties defined in the class (with
    the properties and methods of the base object class. To get any other method you should inherit from the other class
    or define it in the class body. It is preferred to inherit method rather then making them. Use mro() to check the
    method resolution order, __mro__. its also depends on the class inheritance order

#   Python multiple Inheritance is possible.
    To create multiple inheritance its needed to call all class constructors from the subclass constructor
    It should take all parameters that all class should take in order to supply them with the required parameters
    multiple inheritance reached with passing multiple classes to the subclass as argument. in this case super not used
    because there are multiple references (safe) in the subclass

#   Method Resolution Order.
                A
            /       \
        /               \
    B                       C
        \               /
            \       /
                D

    This diagram shows that D do not have direct access to the methods and properties that are presents in A
    Its has access to the methods defined in B and C
    this can be checked using mro() method which will show us the backtrace of the resolution flow

#   Pure functions
    We expect some functionality which separate the code into the data and pure functions
    Pure function should not produce any side effects. It should not interact with outside world
    Its should react always in the same way. The pure functions let us have less buggy code

    map, filter, zip, reduce
    map(*func, list)
    map is used to produce new list depending on the input list

    filter(*func, list)
    filter returns the item which produces a thue value

    zip(iter1, iter2)
    zipes together  iterables, the result is list with tuple as one of its elements

    reduce not a part of inbuild python function. In order to use reduce first we need to import
    from functools import reduce. It is used to apply a particular function on the list elements
    it is easy way to get the sum of all the elements in the provided iterable. It is reduced the sequence to the
    single value

#   lambda expressions (functions like arrow functions in js)
    It is  unanimous function that do not need more than once
    They are do not stored in the memory
    lambda param: action(param)

#   list,  set, dictionary Comprehensions
    list: [param for param in iterable]
    set: {param for param in iterable}
    dict: {key:value for key, value in another_dict.items()}

#   when interpreter reaches to the def key word it is allocate some memory to the body of the function
    then link function name to that memory location. in case when we delete the function  name the memory
    not freed (memory leak)

#   Higher-order function
    this can be tow types
    1. It is a function that accepts function as an argument
    def greet(func)
        func()
    2. It is a function that returns another function
        def greet2():
            def func():

            return func

#   Error handling
    Allows us to keep code running even if there is an error
    try: Always executes this
    except exception as error: if an error this will handle it. in this case it will provide a descriptive message
    error is an object
    else: if no error this block will execute
    finally: This runs at the end of the error handling. Its will always executes
    raise: Allows to make your own descriptive error. Its call buildin exception with the custom message

#   Generators
    range() is generator
    difference between generator and list is that the list is allocate the memory but the generator allocate only
    one item in memory
    Generators are pause (suspend) and resume some functionality
    yield pauses the function and returns to it if we try to interact with it. it keeps last data in memory
    and return it when we call next()
    if we creating the function with the range and yield keyword its returns a generator object
    def generator_function(num):
        for i in range(num):
            yield i

    this will return us a generator
    to us it we should
    for i in generator_function(num)
    to interact with the generator function we should use next() function
    next can be called not more than number specified in the range. otherwise it will thrown error

#   modules
    Every file is module. modules are named in snake-case format like  data_art.py import data_art
    python package is a simply a folder that contains modules import dir.data_art syntax
    in the root of the package folder we should have __init__.py folder in order to inform to the interpreter
    that this is a python package
    hot keys
    import
    from  it used to avoid name collusion
    import as
    from import
    if __name__ == '__main__':
    the __name__ is module name that assigned to it
    the name __main__ interpreter automatically gives to the file that is we running
    it is doing in order to run avoid run the file unless it is not __main__
    to get information about imported module just use help()
    All build-in modules are named Standard Library
    Python Package Index pypi.org <-- secondly check here
    Python Module Index py-modindex.html  <-- first check here
    pip repository
    pip install package_name
    pip uninstall package_name
    True power of python comes from community
    virtualenv is used in order to keep different versions of the package on the same host to solve the dependency
    Some times it is needed if we are using the same package in the different projects
    It is a way to separate universes

#   Versioning
    major. minor. patch
    patch <-- increasing after bug-fixing
    minor <-- increasing after new feature or new release
    major <-- increasing after breaking version or major changes

#   Counter produce a dictionary from iterable where the key is items in iterable and the value their count
    it is a part of collections
    dictionaries by default unordered. Its mean that they are equal each other if there keys order are different.
    In order to solve this we should use OrderedDict

#   array is a module in python. This is more performance then list because it consists from homogeneous items

#   debugging:
    1. Using Linting plugins in Code editors
    2. Using Ide / Text editors
    3. Reading the Errors (exceptions)
    4. using pdb (python debugger)
        import pdb
        pdb.set_trace()
        it is possible to change variable when it is in pdb mode
    5. using print

#   File IO
    open(filename, mode, ...)
        .read() -> Cursor move to the end of the file
        .seek(position) -> moves cursor to the position
        .readline() -> moves cursor to the end of the line
        .readlines() -> converts the file to the list of lines separated by '\n'
        .close() -> in order to close the opened file (mandatory)

    The proper way to work with files is the follows
    with open(filename) as custom_name:
        action

    in this case it is not needed to close the file

    if we don't specify the mode it is by default set to 'r' read mode
    The File IO Flow the following: Only one operation is allowed to be done one the file on each open
    It is impossible to read and write at the same time. you should close the file and reopen it

#   Regular expressions
    It is additional tool to work with string
    They are useful to finding a peace of code in the string
    It can be used to group words in the given string using group() method
    If regular expression doesnt find anything its returns None
    It is possible to get the list of occurrence of the word
    https://regex101.com/ can be useful to assemble the required regular expression
    https://emailregex.com/ example of how we can check email validation

#   Testing in the python
    PEP 8 is a standard guid to code in python
    for testing purpose there is a module called unittest
    To work with unittest we should make class TestMain(unittest.TestCase)
    to run the unittest use unittest.main()
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    Because unittest are not going to the production you can write them without keeping the good
    codding style
    It is possible to make testes for different modules
    py -3 -m unittest to run all testes
    def setUp(self) let you to run a function before every test case
    def tearDown(self) executes et the and of every function
    it is good practice to put whenever if __name__ == '__main__': in order to prevent the execution of
    the tested file
"""