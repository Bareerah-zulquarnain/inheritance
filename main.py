class person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display (self):
        print (self.name)
        print (self.idnumber)

class Employee(person):
    def __init__(self, name, salary, post, idnumber):
        self.salary = salary
        self.post = post

        person.__init__(self, name, idnumber )

a = Employee ('Penguin', 202101401, 15000, "Intern")
a.display()


