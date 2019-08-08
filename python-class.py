import weakref

class User:
    instances = []
    def __init__(self, first_name, last_name, email):
        self.__class__.instances.append(weakref.proxy(self))
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.email = email

    def show_user(self):                                                                         
        print(self.__dict__)   

    def show_all_users():                   
        for instance in User.instances:
            print(instance.__dict__) 

    def __delete__(self):                         
        del self.__dict__
        return "User Deleted"
        
    def update_user(self, new_fname, new_lname, new_email):  
        self.first_name = new_fname
        self.last_name = new_lname
        self.email = new_email

#To Add User
#user = User('fname', 'lname', 'email')

#To Show User
#user.show_user()

#To Show All the Users Listed
#User.show_all_users()

#To Delete User
#user.__delete__()

#To Update User
#user.update_user('newfname', 'newlname', 'newemail')


