# excersise from https://textdoc.co/13Sa2udmAEOzUDyk

class Account():
    
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        self.balance += amount 
        
    def withdraw(self, amount: float) -> None:
        pass
            
    def apply_daily_interest(self):
        pass

class CheckingAccount(Account):
    
    def __init__(self, name: str, balance: float) -> None:
        super().__init__(name, balance)
        
    def __str__(self) -> str:
        return f"CheckingAccount(name={self.name}, balance=${self.balance})"

    def withdraw(self, amount: float) -> None:
        if not self.balance - amount < 0:
            self.balance -= amount
            
class SavingAccount(Account):
    
    def __init__(self, name: str, balance: float, interest_rate: float) -> None:
        super().__init__(name, balance)
        if interest_rate > 0:
            self.interest_rate = interest_rate

    def __str__(self) -> str:
        return f"SavingAccount(name={self.name}, balance=${self.balance}, interest_rate={self.interest_rate})"

    def apply_daily_interest(self) -> None:
        self.balance += (self.interest_rate / 100 * self.balance)

class CreditAccount(Account):
    
    def __init__(self, name: str, balance: float, interest_rate: float, credit_limit: int) -> None:
        super().__init__(name, balance)
        if interest_rate > 0:
            self.interest_rate = interest_rate
        self.credit_limit = credit_limit

    def __str__(self) -> str:
        return f"CreditAccount(name={self.name}, balance=${self.balance}, interest_rate={self.interest_rate}, credit_limit=${self.credit_limit})"

    def withdraw(self, amount: float) -> None:
        if self.balance - amount > -self.credit_limit:
            self.balance -= amount

    def apply_daily_interest(self) -> None:
        if self.balance < 0:
            self.balance += (self.interest_rate / 100 * self.balance)

class Bank():
 
    def __init__(self) -> None:
        self.accounts = []

    def open_account(self) -> None:
        account_type: str = self._account_type()
        match account_type:
            case "checking":
                self._open_checkingAccount()
            case "saving":
                self._open_savingAccount()
            case "credit":
                self._open_creditAccount()
            case _:
                raise ValueError("unsupported account")

    # 4 helper functions to support open_account function.
    def _account_type(self) -> str:
        return input("account type to open: ")
    
    def _open_checkingAccount(self) -> None:
        name: str = input("name: ")
        balance = float(input("balance: "))
        self.accounts.append(CheckingAccount(name, balance))

    def _open_savingAccount(self) -> None:
        name: str = input("name: ")
        balance = float(input("balance: "))
        interest_rate = float(input("interest rate in %: ").rstrip("%"))
        self.accounts.append(SavingAccount(name, balance, interest_rate))

    def _open_creditAccount(self) -> None:
        name: str = input("name: ")
        balance = float(input("balance: "))
        interest_rate = float(input("interest rate in %: ").rstrip("%"))
        credit_limit = int(input("credit limit: "))
        self.accounts.append(CreditAccount(name, balance, interest_rate, credit_limit))

    # display and save to file , accounts
    def display_accounts(self) -> None:
        for index, account in enumerate(self.accounts):
            print(f"{index}: {account}")
            
    def save_accounts(self) -> str:
        with open("accounts.txt", "w") as f:
            for index, account in enumerate(self.accounts):
                f.write(f"{index}: {account}\n")

    # compute functions 
    def apply_daily_interest(self) -> None:
        for account in self.accounts:
            account.apply_daily_interest()
                
    def total_cash(self) -> None:
        total_cash: float = 0
        for account in self.accounts:
            if account.balance > 0:
                total_cash += account.balance
        print(total_cash)
               
    def total_credit(self) -> None:
        total_credit: float = 0
        for account in self.accounts:
            if account.balance < 0:
                total_credit += account.balance
        print(total_credit)


def main():
    bank = Bank()
    bank.open_account()
    bank.open_account()
    bank.apply_daily_interest()
    bank.display_accounts()
    bank.save_accounts()


if __name__ == "__main__":
    main()