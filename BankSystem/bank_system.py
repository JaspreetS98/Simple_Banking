from customer import Customer
from admin import Admin

accounts_list = []
admins_list = []

class BankSystem(object):                                                      #Create lists for data
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self):                                                  #loding customers data
        databasecustomers=open("customersdata.csv","r")                        #opening database file as reading mode
        line=databasecustomers.readline()                                      #reading line
        while line!="":                                                        #reading line unless it is empty    
            customerdata=line.split(",")                                       #spliting each part using commas
            customer=Customer((customerdata[0]),(customerdata[1]),(customerdata[2]),(customerdata[3]),(customerdata[4]),(customerdata[5]),(customerdata[6:10]))
            self.accounts_list.append(customer)                                #creating account
            line=databasecustomers.readline()
        databasecustomers.close()
                                                               
        databaseadmin=open("admindatabase.csv","r")                            #Loading Admins data
        line=databaseadmin.readline()                                          #reading line
        while line!="":                                                        #reading line unless it is empty    
            admindata=line.split(",")                                          #pliting each part using commas
            admin=Admin((admindata[0]),(admindata[1]),(admindata[2]),(admindata[3]),(admindata[4]),(admindata[5:9]))
            self.admins_list.append(admin)                                     #creating account
            line=databaseadmin.readline()
        databaseadmin.close()


    def admin_login(self, username, password):                                 #Admin login function 
        found_admin = self.search_admins_by_name(username)                     #searching admin name 
        msg = "\n Login failed"
        if found_admin != None:                                                #if name is not none
            if found_admin.get_password() == password:                         #if name is found then check password
                msg = "\n Login successful"
                return msg, found_admin                                        #if name and password are right send back    
      
    def search_admins_by_name(self, admin_username):                           #Search for a admin object  
        found_admin = None
        for a in self.admins_list:                                             #checking list of names in our database 
            username = a.get_username()                                        #if given name is right then saving it
            if username == admin_username:
                found_admin = a
                break                                                          #if found exit loop
        if found_admin == None:                                                #if not found then found admin is none.
            print("\n The Admin %s does not exist\n" %admin_username)#printing error  
        return found_admin                                                     #returning if the name is found    
        
    def search_customers_by_name(self, customer_lname):                        #Search for a customer object  
        found_customer = None
        for a in self.accounts_list:                                           #checking list of last names 
            name = a.get_last_name()                                           #if given name is right then saving it
            if name == customer_lname:
                found_customer = a
                break                                                          #if found break loop
        if found_customer == None:                                             #if not found then found customer is none.
            print("\nThe customer %s does not exist\n" %customer_lname)#printing error  
        return found_customer                                                  #returning if the name is found 

    def main_menu(self):                                                       #printing the options at start              
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        try:
            option = int(input ("Choose your option: "))
            return option
        except ValueError:
            print()
            print("Your chosen option is Incorrect. Please input 1 / 2 / 3")


    def run_main_options(self):                                                #Admin Login
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                try:
                    username = input ("\n Please input admin username: ")
                    password = input ("\n Please input admin password: ")          
                    msg, admin_obj = self.admin_login(username, password)
                    print(msg)
                    if admin_obj != None:
                        self.run_admin_options(admin_obj)                      #Call admin menu
                except:
                    print ("\n Login failed")                           
            elif choice == 2:
                loop = 0
                print ("Thank-You for stopping by the bank")
                
            
    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        sender = self.search_customers_by_name(sender_lname)                   #searching sender
        if sender != None:
            receiver = self.search_customers_by_name(receiver_lname)           #searching receiver
            if receiver != None:   
                receiver_no = receiver.get_account_no()                        #searching receiver_account_no
                if receiver_account_no == receiver_no:
                        sender.withdraw(amount)                                #take out money from sender
                        receiver.deposit(amount)                               #transfer money to receiver
                        print("The transfer is terminated")
                        




    def admin_menu(self, admin_obj):                                           #print options for admin menu
         print (" ")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations")
         print ("3) Customer profile settings")
         print ("4) Admin profile settings")
         print ("5) Delete customer")
         print ("6) Print all customers detail")
         print ("7) Management report")
         print ("8) Sign out")
         print (" ")
         try:                                                                  #escape error
             option = int(input ("Choose your option: "))
             return option
         except ValueError:
             print ("Choose another option") 


    def run_admin_options(self, admin_obj):                                    #options for admin menu
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")       #get info for transfer
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount) #call transfer function
            elif choice == 2:
                customer_name=input("\n Please input customer surname: \n")            
                customer = self.search_customers_by_name(customer_name)        #finding customer
                if customer != None:
                      customer.run_account_options()                           #open account options menu with customer
                
            elif choice == 3:
                customer_name = input("\nPlease input customer surname :\n")
                customer = self.search_customers_by_name(customer_name)        #finding customer
                if customer!=None:
                    customer.run_profile_options()                             #open profile ptions menu with customer
            elif choice == 4:
               admin_obj.run_profile_options()                                 #open profile ptions menu with admin
                
            elif choice == 5:
                if admin_obj.has_full_admin_right() == "True":
                    customer_name = input("\nPlease input customer surname you want to delete :\n")
                    customer_account = self.search_customers_by_name(customer_name) #finding customer
                    if customer_account != None:
                        self.accounts_list.remove(customer_account)            #delete customer
                        print("\n Customer %s has been removed from the system \n"%customer_name)
                else:
                        print("\nOnly administrators with full admin rights can remove a customer from the bank system\n")
                
            elif choice == 6:
                self.print_all_accounts_details()                              #print all account's details
                
            elif choice == 7:
                total_balance = 0
                total_interest_balance = 0
                total_overdraft = 0
                for c in self.accounts_list:                                   #loop to calculate the totals for the report
                    if c.get_balance() < 0:
                        total_overdraft += c.get_balance()                     #calculate total overdraft
                    else:
                        total_balance += c.get_balance()                       #calculate total balance
                        total_interest_balance += c.get_balance()*c.get_interest()   #calculate total interest
                print(f" Total costumers: {len(self.accounts_list)}")
                print(f" Customers total current balance = {total_balance:.2f}")
                print(f" Annual interest to the costumers: {(total_interest_balance):.2f}")
                print(f" Total overdraft costumers: {total_overdraft:.2f}")
            
            
            elif choice == 8:        
                loop = 0                                                       #exit menu
                print ("Exit account operations")


    def print_all_accounts_details(self):                                      #loop to print all accounts
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()                                              #call the print funtion for details
                print("------------------------")


app = BankSystem()
app.run_main_options()
