class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.isTrue = True
    
    def deposito(self, amount):
        if self.isTrue:
            self.balance += amount
            print(f'{self.account_holder}. Se ha depositado {amount}. Saldo actual {self.balance}')
        else:
            print('Cuenta inactiva')
    
    def withdraw(self, amount):
        if self.isTrue and self.balance > 0:
            self.balance -= amount
            print(f'{self.account_holder}. Se ha realizado un retirdo de {amount}. Su saldo actual es de {self.balance}')
        else:
            print(f'{self.account_holder}. Su saldo es insuficiente. Saldo actual {self.balance}')
            
        
    def deactivateAccount(self):
        self.isTrue = False
        print('La cuenta ha sido desactivada')
        
    def activateAccount(self):
        self.isTrue = True
        print('La cuenta ha sido activada')
        
movimiento = BankAccount('Pablo Lara', 50000)
movimiento.deposito(1500)
movimiento.withdraw(1000)
movimiento.deactivateAccount()
movimiento.activateAccount()
    