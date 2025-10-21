class Student:
    def __init__(self, id, first, last):
        self.id = id
        self.first = first
        self.last = last 
    
    def set_GPA(self, GPA):
        self.GPA = GPA
        if self.GPA < 2.0:
            self.probation = True
            print(f"{self.first} {self.last} is in bad academic standing.")
        else:
            self.probation = False
            print(f"{self.first} {self.last} is in good academic standing.")
        return self.probation
    
student_1 = Student(1, "John", "Johnson")
student_2 = Student(2, "Jane", "Doe")
student_3 = Student(3, "Kimberly", "Kim")
student_4 = Student(4, "Will", "Williams")

enrolled_students = [student_1, student_2, student_3, student_4]

student_probation = {}

def display_all(enrolled_students):
    for student in enrolled_students:
        print(f"{student.first} {student.last}, ID: {student.id}")

def enter_GPA(enrolled_students, student_probation):
    answer = int(input("Please enter the ID of the student whose GPA you'd like to edit: "))
    for student in enrolled_students:
        if answer == student.id:
            #Code when right student is found
            print(f"You want to edit the GPA of {student.first} {student.last}.")
            answer2 = float(input("Type in the new GPA: "))
            probation_status = student.set_GPA(answer2)
            student_probation[student.id] = probation_status
            break

def display_probation(student_probation):
    answer = int(input("Enter the id of the student who you want to look up: "))
    if answer in student_probation:
        #If id is in dictionary
        if student_probation[answer] == True:
            print("This student is under academic probation.")
        else:
            print("This student is in good academic standing.")
    else:
        print("This student does not exist or has not been assigned a GPA.")

while(True):
    answer = int(input("\nPlease choose one of the following options: \n" \
    "1. See the list of all enrolled students.\n" \
    "2. Enter a student's GPA. \n" \
    "3. Do a quick lookup to see if a student is under academic probation."))
    #"4. Enroll a new student.\n" 
    if(answer == 1):
        display_all(enrolled_students)
    elif(answer == 2):
        enter_GPA(enrolled_students, student_probation)
    elif(answer == 3):
        display_probation(student_probation)
    else:
        print("Invalid input.")