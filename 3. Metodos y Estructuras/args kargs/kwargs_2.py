def print_info(**kwargs):
    for key, value in kwargs.items():
     print(f"{key}: {value}")   

print_info(name='carlos', age='30', city='medellin')
    