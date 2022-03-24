from Ex16Person import Person
class Customer(Person):
    def __init__(self, first_name, surname, money, consumer_personality, consumer_habits):
        super().__init__(first_name, surname) #why not just call person function instead of super?
        self.money = money
        self.consumer_personality = consumer_personality
        self.consumer_habits = consumer_habits


    def Customer_type(self):
        print(f"This Customer is called {self.first_name} {self.surname} has {self.money} of money and they are {self.consumer_personality} and they {self. consumer_habits}.")