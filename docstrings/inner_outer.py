x = 'global' # Variable global

# External function
def outer_function():
    x = 'enclosing'
    print(x)
    
    
    # Internal function
    def inner_function():
        x = 'local' # Variable local
        print(x)
    inner_function()
    print(x)

outer_function()
print(x)
