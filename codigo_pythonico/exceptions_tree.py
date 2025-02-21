def print_exception_hierarchy(exception_class, ident=0):
    print(' '*ident + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, ident + 4)

print_exception_hierarchy(Exception)
    