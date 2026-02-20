class Atm:
    # constructor
    def __init__(self,account_number,pin,balance):
        self.account_number = account_number    # Object Attribute
        self.pin = pin
        self.balance = balance

    # Method to check pin
    def check_pin(self,entered_pin):
         if entered_pin == self.pin:
             return True
         else:
             return False
         
    # Method to deposit Money
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposit Successful. Your Balance is : {self.balance}")
    
    # Method to Withdraw Money
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance.")
        else:    
            self.balance-=amount
            print(f"Withdraw Successul. Your Balance is : {self.balance}")

    # check Balance
    def check_balance(self):
        print(f"Current Balance is {self.balance}")

# Creating an instance of the Atm class
user1=Atm("123456789","1234",1000)

entered_pin=input("Enter Your Pin : ")
if user1.check_pin(entered_pin):
    while True:
        print("---ATM--- Menu")
        print("1.  Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice=input("Enter Your Choice :  ")
        if choice=="1":
            user1.check_balance()
        elif choice=="2":
            amount=float(input("Enter amount to deposit  : "))
            user1.deposit(amount)
        elif choice=="3":
            amount=float(input("Enter amount to withdraw : "))
            user1.withdraw(amount)
        elif choice=="4":
            print("Thank You for using the ATM. Goodbye..!")
            break
        else:
            print("Invalid Choice. Please Try Again.")
else:
    print("Incorrect Pin. Access Denied.")