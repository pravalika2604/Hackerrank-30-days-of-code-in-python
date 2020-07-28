

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    # firstname=Person.firstName
    # lastname=Person.lastName
    # idNum=Person.idNum
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if 90<=avg<=100:
            grade = 'O'
        if 80<=avg<90:
            grade = 'E'
        if 70<=avg<80:
            grade = 'A'
        if 55<=avg<70:
            grade = 'P' 
        if 40<=avg<55:
            grade = 'D'
        if avg<40:
            grade = 'T'
        return grade
            



