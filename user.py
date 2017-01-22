class User():
    """A simple attempt to create a user."""

    def __init__(self, first_name, last_name, age, city, country):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.country = country
        self.login_attempts = 0

    def greet_user(self):
        """Greet the user."""
        print("Hello " + self.first_name.title() + " " + self.last_name.title() +
              "!")

    def describe_user(self):
        """Describe the user."""
        print(self.first_name.title() + " " + self.last_name.title() + " is " +
              str(self.age) + " years old" + " and" + " lives in " +
              self.city.title() + ", " + self.country.title())

    def increment_login_attempts(self):
        """Increment the login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to zero."""
        self.login_attempts = 0

    def number_of_login_attempts(self):
        """Print the number of login attempts."""
        print("You have tried to login " + str(self.login_attempts) + " times!")

class Privileges():
    """Hold privileges for users."""
    def __init__(self, user_privileges):
        """Initialize the attributes."""
        self.user_privileges = user_privileges

    def show_privileges(self):
        """Print privileges."""
        print("Here are your privileges: " + self.user_privileges)


class Admin(User):
    """Type of user with elevated priveleges."""
    def __init__(self, first_name, last_name, age, city, country, privileges):
        super().__init__(first_name, last_name, age, city, country)
        self.privileges = Privileges('can add user, delete post and ban user')




#new_user = User('Allen', 'Rohl', '42', 'Wake Forest', 'North Carolina')
new_admin = Admin('Allen', 'Rohl', '42', 'Wake Forest', 'North Carolina', 'can add user, delete post and ban user')

#new_user.greet_user()
new_admin.greet_user()
new_admin.privileges.show_privileges()
#new_user.describe_user()

#new_user.increment_login_attempts()
#new_user.number_of_login_attempts()
#new_user.reset_login_attempts()
#new_user.number_of_login_attempts()
