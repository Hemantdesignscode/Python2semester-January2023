
class Higher_Studies_School():
    def __init__(self, univeristy):
        self.university = univeristy
    
class Department(Higher_Studies_School):
    def __init__(self, univeristy, department):
        Higher_Studies_School.__init__(self, univeristy)
        self.department = department

class Programming_Language(Department):
    def __init__(self, university, department, program_language):
        Department.__init__(self, university, department)
        self.program_language = program_language
    
    def printstudy(self):
        print("\nI am in",self.university,"my department is",self.department,"and I am learning",self.program_language,"\n")

career_path = Programming_Language("Georgia State University", "Computer Science", "Python")
career_path.printstudy()