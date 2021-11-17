class School:
    def __init__(self, name, level, numberOfStudent):
        self.name = name
        self.level = level
        self.numberOfStudent = numberOfStudent

    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.level
    
    def getNumberOfStudent(self):
        return self.numberOfStudent
    
    def setNumberOfStudent(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents

    def __repr__(self):
        SchoolRepr = 'A {} school named {} with {} students.'.format(self.level, self.name, self.numberOfStudent)
        return SchoolRepr


#------ TEST CLASS SCHOOL WITH THE CODE BELOW --------:

# mySchool = School("Codecademy", "high", 100)
# print(mySchool)
# print(mySchool.getName())
# print(mySchool.getLevel())
# mySchool.setNumberOfStudent(200)
# print(mySchool.getNumberOfStudent())

