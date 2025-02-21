def outer_functiom():
    x = 'enclosing'
    
    def inner_function():
        nonlocal x 
        x = 'modified'
        print(f'El valor en inner de x es: {x}')
        
    inner_function()
    print(f'El valor de outer es: {x}')
    
outer_functiom()