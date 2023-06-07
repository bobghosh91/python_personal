class Emloyee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def getfullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Emloyee('bgt','huk',500)
emp_2 = Emloyee('kk','ji',866)

print(Emloyee.getfullname(emp_1))