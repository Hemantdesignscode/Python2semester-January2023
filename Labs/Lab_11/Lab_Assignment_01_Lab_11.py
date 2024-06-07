
class Company():
    def __init__(self, company):
        self.company = company
    
class Department():
    def __init__(self, department):
        self.department = department
    
class Position(Company, Department):
    def __init__(self, company, department, position):
        Company.__init__(self, company)
        Department.__init__(self, department)
        self.position = position
    
    def printcompanyplacement(self):
        print("\nI am in",self.company, self.department,"and my position is",self.position,"\n")

career = Position("Microsoft", "Information Technology", "Intermediate Multiplatform App Coder and Tester")
career.printcompanyplacement()