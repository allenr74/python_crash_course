#restaurant.py

class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize name and age attributes."""
        self.name = name
        self.cuisine = cuisine
        self.customers = 0

    def open_restaurant(self):
        """Simulate a restaurant opening."""
        print(self.name.title() + " is now open.")

    def describe_restaurant(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " serves " + self.cuisine.title() + " cuisine.")

    def number_served(self):
        """Print a statement showing the number of customers served."""
        print("This restaurant has served " + str(self.customers) + " people.")

    def set_number_served(self, people):
        """Used to set the number of people served by the restaurant."""
        self.customers = people

    def increment_number_served(self, clients):
        """Used to increment the number of people served."""
        self.customers += clients

class IceCreamStand(Restaurant):
    """Models an ice cream stand."""
    def __init__(self, name, cuisine, flavors):
        """Initialize aspects of the parent class"""
        super().__init__(name, cuisine)
        self.flavors = flavors

    def display_flavors(self,):
        print("We serve " + self.flavors + " at " + self.name.title() +
        " ice cream stand.")

#restaurant = Restaurant('mood for', 'american')
#restaurant.open_restaurant()
#restaurant.set_number_served(45)
#restaurant.increment_number_served(15)
#restaurant.number_served()

ice_cream_stand = IceCreamStand('glaciers', 'ice cream', 'vanilla, chocolate and strawberry')
ice_cream_stand.open_restaurant()
ice_cream_stand.display_flavors()
