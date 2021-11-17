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

class Primary(School):
    def __init__(self, name, numberOfStudent, pickupPolicy):
        super().__init__(name,'primary', numberOfStudent)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        PrimaryRepr = super().__repr__()
        return PrimaryRepr + " The pickup policy is {}.".format(self.pickupPolicy)

class Middle(School):
    def __init__(self, name, level, numberOfStudent):
        super().__init__(name, level, numberOfStudent)

#------ TEST CLASS SCHOOL WITH THE CODE BELOW --------:

# mySchool = School("Codecademy", "high", 100)
# print(mySchool)
# print(mySchool.getName())
# print(mySchool.getLevel())
# mySchool.setNumberOfStudent(200)
# print(mySchool.getNumberOfStudent())

#------ TEST CLASS PRIMARY WITH THE CODE BELOW --------:

# testSchool = Primary("Codecademy", 300, "Pickup Allowed")
# print(testSchool.getPickupPolicy())
# print(testSchool)
