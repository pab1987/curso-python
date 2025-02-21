x = 100 # variable global

def local_function():
    x = 10 # Variable local
    print(f'El valo de la variable local x es: {x}')
    
def show_global():
    print(f'El valor de la variable global x es: {x}')
local_function()
show_global()



