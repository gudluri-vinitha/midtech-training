class Bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def show_balance(self):
        print("owner:" ,self.owner)
        print("balance:",self.__balance)
account1=Bankaccount("Ravi",5000)
account1.show_balance()     
#another example
class BankAccount2:

    def __init__(self, owner, balance):
        self.owner = owner
        self._account_type = "Savings"
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw Success")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)


# Create object
account = BankAccount2("John", 3637)

# Display details
print("Owner:", account.owner)
print("Account Type:", account._account_type)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(400)

# Show balance
account.show_balance()


#another task for encapsulation

class Student:
    def __init__(self, name, age, marks, result):
        self.__name = name
        self.__age = age
        self.__marks = marks
        self.__result = result

    def details(self):
        print("Name   :", self.__name)
        print("Age    :", self.__age)
        print("Marks  :", self.__marks)
        print("Result :", self.__result)


student1 = Student("Ravi", 20, 75, "Pass")


student1.details()