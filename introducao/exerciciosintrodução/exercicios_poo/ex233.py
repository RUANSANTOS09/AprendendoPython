class AccountBanking:
    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def get_extract(self):
        print(f'{self.__holder} possui saldo de R$ {self.__balance}')

class AccountSavings(AccountBanking):
    def __init__(self, holder, balance, yield_rate):
        self.__year_rate = yield_rate
        super().__init__(holder, balance)

    def calculate_yield(self):
        return self.get_balance() * self.__year_rate

my_account_savings = AccountSavings('Ruan',17000, 0.05 )
print(f' Proprietario da conta: {my_account_savings.get_holder()}\n saldo sem a taxa: R${my_account_savings.get_balance()}\n saldo com a taxa: R$ {my_account_savings.calculate_yield()}')