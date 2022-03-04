class cat:

    def __init__(self,make_sound,colour,personality):
        self.make_sound = make_sound
        self.colour = colour
        self.personality = personality

    def about_my_cat(self):
        print(f"My cat is {self.colour} and {self.personality}. When my cat is hungry they {self.make_sound}.")

