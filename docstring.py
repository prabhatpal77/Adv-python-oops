# Documentation String:- Documentation string of a class is used to provide description about the class.
# Within the class syntax documentation string is optional but it is highly recommended to define documentation
# string with in the class syntax. We can access documentation string of a class by, "__doc__" default attribute
# of a class.
print("begin")
class Test:
    """Sample class to test doc str"""
print(Test.__doc__)
print(list.__doc__)
print("end")

# documentation string should be the first statement in the class syntax..
