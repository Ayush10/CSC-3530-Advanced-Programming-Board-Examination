import smtplib
from email.message import EmailMessage


class Student:
    def __init__(self):
        self.IUKL_Code = 0
        self.Own_Name = ""
        self.Student_Phone_Number = 0
        self.Student_Gender = ""
        self.Student_Email = ""
        self.Student_Grade = 0

    # getter
    def getIUKL_Code(self):
        return self.IUKL_Code

    def getOwn_Name(self):
        return self.Own_Name

    def getStudent_Phone_Number(self):
        return self.Student_Phone_Number

    def getStudent_Gender(self):
        return self.Student_Gender

    def getStudent_Email(self):
        return self.Student_Email

    def getStudent_Grade(self):
        return self.Student_Grade

    # setter
    def setIUKL_Code(self, newValue):
        self.IUKL_Code = newValue

    def setOwn_Name(self, newValue):
        self.Own_Name = newValue

    def setStudent_Phone_Number(self, newValue):
        self.Student_Phone_Number = newValue

    def setStudent_Gender(self, newValue):
        self.Student_Gender = newValue

    def setStudent_Email(self, newValue):
        self.Student_Email = newValue

    def setStudent_Grade(self, newValue):
        self.Student_Grade = newValue

    def Input_Student_Information(self):
        print("Enter Detail")
        self.IUKL_Code = int(input("Enter IUKL Code : "))
        self.Own_Name = input("Enter Name (Name Must be in Firstname_Lastname) : ")
        self.Student_Phone_Number = int(input("Enter your Phone number : "))
        self.Student_Gender = input("Gender : ")
        self.Student_Email = input("Email : ")
        self.Student_Grade = input("Enter Grade : ")

    def display_Student_Information(self):
        print("===========================")
        print("Student Information")
        print("===========================")
        print("Student IUKL ID : " + str(self.IUKL_Code))
        print("Student Name : " + self.Own_Name)
        print("Student Phone Number : " + str(self.Student_Phone_Number))
        print("Student Gender : " + self.Student_Gender)
        print("Student Email : " + self.Student_Email)
        print("Student Grade : " + self.Student_Grade)

    def registrations(self):
        password = "peterkarki99@GOOGLE"
        message = EmailMessage()
        contain = "Student Info : \n" + "Student IUKL ID : " + str(
            self.IUKL_Code) + "\n" + "Student Name : " + self.Own_Name + "\n" + "Student Phone Number : " + str(
            self.Student_Phone_Number) + "\n" + "Student Gender : " + self.Student_Gender + "\n" + "Student Email : " + self.Student_Email + "\n" + "Student Grade : " + self.Student_Grade
        message.set_content(contain)
        message['Subject'] = "Registration"
        message['From'] = "peterkarki99@gmail.com"
        message['To'] = "peter.karki0422@gmail.com"
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("peterkarki99@gmail.com", password)
        server.send_message(message)
        server.quit()
        print("Email Sent")


test = Student()
test.Input_Student_Information()
test.display_Student_Information()
test.registrations()