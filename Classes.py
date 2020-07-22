import datetime
class User:
    def __init__(self,full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        self.birthdate = birthday[:4] + '/' + birthday[4:6] + '/' + birthday[6:]
        #Extract first and last names
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

        # def age(self):

user = User('Aditya Gole', '20020225')
print(user.name)
print(user.birthdate)
 
