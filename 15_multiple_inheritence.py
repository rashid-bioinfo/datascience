# Multiple Inheirtance

class Father:
    def gardening(self):
        print("I love gardening")
    
    def skills(self):
        print("programming")    

class Mother:
    def cooking(self):
        print("I love cooking")

    def skills(self):
        print("Teaching")

class Child(Father, Mother):
    def sports(self):
        print("I love sports")
    
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Coding")

c = Child()

c.gardening()
c.cooking()
c.sports()
c.skills()