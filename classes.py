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

#class inheritance
class Student(Person):
  def __init__(self, fname, lname, gender, salary, year, form):
    super().__init__(fname, lname, gender, salary)
    self.graduationyear = year  
    self.form = form
    
    def computed(self):
        pass
        
person1 = Person("david", "hope", "male", 10000)
person2 = Person("richard","isaac","female",20000)
student = Student("david", "hope","male",20000, 1992,"s.2")
print(person1.fullname())
print(person2.increment_salary())
print(student.graduationyear)
print(student.form)
print(student.fullname())