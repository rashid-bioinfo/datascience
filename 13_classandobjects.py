# Class and Objects

class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if (self.occupation == "Tennis Player"):
            print(f"{self.name} plays Tennis")
        elif (self.occupation == "Acting"):
            print(f"{self.name} shoots film")
    
    def speak(self):
        print(f"{self.name} speaks about {self.occupation}")

tom = Human('Tom Cruise', 'Acting')
tom.do_work()
tom.speak()

sara = Human('Sarah', 'Tennis Player')
sara.do_work()
sara.speak()