class Calculator:
    @staticmethod
    def add(*args) -> int:
        return args[0] + args[1]
    
    print(add(1,1))