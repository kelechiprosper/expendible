class Person:
    def __init__(self, name):
            self.name = name

    def talk(self):
            print(f"Hi i am {self.name}")


sammy = Person("Sammy")
sammy.talk()

stan = Person("stan bush")
stan.talk()