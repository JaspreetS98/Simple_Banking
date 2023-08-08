class Person(object):

    def __init__(self, fname,lname, password, address = [None, None, None, None]):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.address = address
            
    def update_first_name(self, fname):                                        #function to update first name
        self.fname = fname
    
    def update_last_name(self, lname):                                         #function to update last name
        self.lname = lname
                
    def get_first_name(self):                                                  #function to extract first name
        return self.fname
    
    def get_last_name(self):                                                   #function to extract last name
        return self.lname
        
    def update_address(self,door,street,city,postcode):                        #function to update address
        self.address[0]=door                                                   
        self.address[1]=street
        self.address[2]=city
        self.address[3]=postcode
        
    def get_address(self):                                                     #function to extract address
        return self.address       

    def update_password(self, password):                                       #function to update password
        self.password = password
    
    def get_password(self):                                                    #function to extract password
        return self.password    

    def print_details(self):                                                   #funtion to print details 
        print("--------------------------------")
        print("--------------------------------")
        print("First Name: %s" %self.fname)
        print("Last Name: %s" %self.lname)
        print("Address: %s" %self.address[0])
        print("         %s" %self.address[1])
        print("         %s" %self.address[2])
        print("         %s" %self.address[3])
    
    def profile_settings_menu(self):                                           #funtion to print profile setting menu options
         print (" ")
         print ("Your Profile Settings Options Are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name")
         print ("2) Update Address")
         print ("3) Update Password")
         print ("4) Print details")
         print ("5) Back")
         print (" ")
         try:
             option = int(input ("Choose your option: "))
             return option
         except ValueError:
             print("Please input correct option")
        
    def run_profile_options(self):
        loop = 1           
        while loop == 1:
            choice = self.profile_settings_menu()
            if choice == 1:
                fname=input("\n Please enter new first name\n: ")              #getting new first name
                self.update_first_name(fname)
                lname=input("\n Please enter new last name\n: ")               #getting new last name
                self.update_last_name(lname)
            elif choice==2:
                door = input("\nEnter door number : ")                         #getting new address
                street = input("\nEnter street: ")
                city = input("\nEnter city: ")
                postcode = input("\nEnter postcode: ")              
                self.update_address(door,street,city,postcode)
            elif choice == 3:
                password=input("\n Please enter new password\n: ")             #getting new password
                self.update_password(password)  
            elif choice == 4:
                self.print_details()                                           #print details
            elif choice == 5:  
                loop = 0                                                       #close run_profile_options menu 
