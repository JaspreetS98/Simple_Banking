from person import Person
class Customer(Person):
    def __init__(self, fname, lname, password, balance, account_no, account_type, address = [None, None, None, None]):
        super().__init__(fname,lname, password, address)
        self.balance = float(balance)
        self.account_no = account_no
        self.account_type = account_type
    
    def deposit(self, amount):
        self.balance+=amount                                                   #adding money to the account
              
    def withdraw(self, amount):
        if self.balance>=amount and amount>0:                                  #if balance is more than amount then subracting amount from balance
            self.balance-=amount
        elif self.balance<amount and amount>0:                                 #if balance is less than amount calling overdrafrt method
            print ("\n You'll have to use Overdraft Services \n")
            self.overdraft(amount)
        else:   
            print("the amount is negative")
           
            
    def overdraft(self,amount):                                                #overdraft if balance is less than  amount 
        if self.account_type=="Basic" or self.account_type=="Student":
            print ("\n You do not have Overdraft Services \n")                 #No overdraft for basic and student account
        elif self.account_type=="Classic" and (self.balance-amount>=-2000.00):
            self.balance-=amount
        elif self.account_type=="Classic" and (self.balance-amount<-2000.00):
            print("\n Overdraft Limit is 2000 for Classic Account \n")         #overdraft limit of 2000 for classic acount.
        elif self.account_type=="Business" and (self.balance-amount>=-1000.00):
            self.balance-=amount
        elif self.account_type=="Business" and (self.balance-amount<-1000.00):
            print("\n Overdraft Limit is 1000 For Business Account \n")        #overdraft limit for business account is 1000.
                          
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)                  #function to print the account balance
        
    def get_balance(self):                                                     #function to extract account balance
        return self.balance
    
    def get_account_no(self):                                                  #function to extract account number
        return self.account_no
    
    
    def get_interest(self):                                                    #function to know which interest rate to use
        if self.get_account_type() == "Basic":
            return 0.01
        if self.get_account_type() == "Classic" or self.get_account_type() == "Student":
            return 0.03
        if self.get_account_type() == "Business":
            return 0.05
    
    def get_account_type(self):                                                #function to extract account type
        return self.account_type
            
    
    def print_details(self):                                                   #function to print more details
        super().print_details()
        bal = self.get_balance()
        acctype = self.get_account_type()
        accno = self.get_account_no()
        print("Account balance: %.2f" %bal)
        print("Account Type : %s" %acctype)
        print("Account No. : %s" %accno)
        print(" ")

    def account_menu(self):                                                    #menu with customer main operations
                 print (" ")
                 print ("Your Transaction Options Are:")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("1) Deposit money")
                 print ("2) Check balance")
                 print ("3) Withdraw money")
                 print ("4) Back")
                 print (" ")
                 try:                                                          #escape error
                         option = int(input ("Choose your option: "))
                         return option
                 except ValueError:
                         print()
                         print("Incorrect input")
                
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                try:                                                           #escape error
                    amount=float(input("\nPlease enter amount to be deposited\n: "))
                    if amount>0:                                               #amount to deposit / can't be a negative number
                        deposit = self.deposit(amount)
                    else:                                                      #informing to use another amount to withdraw
                        print("retry")
                        self.print_balance()
                except ValueError:
                    print("Incorrect Amount")
            elif choice == 2:
                balance = self.print_balance()
            elif choice == 3:
                balance = self.print_balance()
                try:                                                           #escape error
                    amount=float(input("\n Please enter amount to be Withdrawn \n: ")) #asking money to be withdrawn from the account
                    withdraw = self.withdraw(amount)
                    self.print_balance()
                except ValueError:
                    print("Incorrect Amount")
            elif choice == 4:
                loop = 0
                print ("Exit account operations")
                       