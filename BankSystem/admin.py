from person import Person
class Admin(Person):
    
    def __init__(self, fname, lname, password, user_name, full_rights, address = [None, None, None, None]):
        super().__init__(fname,lname, password, address)
        self.user_name = user_name
        self.full_admin_rights = full_rights
    
    def set_username(self, username):                                          #function to change username
        self.user_name = username
        
    def get_username(self):                                                    #function to extract first name
        return self.user_name
        
    def set_full_admin_right(self, admin_right):                               #function to change admin rights
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):                                            #function to extract first name
        return self.full_admin_rights

