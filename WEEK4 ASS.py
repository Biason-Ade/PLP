class Person:
    def __init__(self, name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print('Person Name:', self.name, ', Age: ', self.age, ', Gender: ', self.gender)

p1 = Person('Collins', 23, 'Male')
p1.introduce()
