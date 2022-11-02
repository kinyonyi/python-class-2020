class Person():
    multiplier = 1.1
    def __init__(self, fname, lname, gender, salary):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.salary = salary
        
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
    
    def increment_salary(self):
        increased = self.multiplier * self.salary
        return "{}".format(increased)
        
person1 = Person("david", "hope", "male", 10000)
person2 = Person("richard","isaac","female",20000)
print(person1.fullname())
print(person2.increment_salary())