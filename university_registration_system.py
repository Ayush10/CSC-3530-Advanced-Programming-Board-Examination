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
        self.percentage = int(input("Enter Percentage : "))
        self.Student_Grade = self.categ(self.percentage)
        self.discount, self.category = self.discountprice(self.Student_Grade)

    def categ(percentage):
        if (percentage > 80):
            return 'A'
        elif (percentage > 70 and percentage <= 80):
            return 'B'
        elif (percentage > 60 and percentage <= 70):
            return 'C'
        elif (percentage <= 60):
            return 'D'

    def discountprice(self, grade):
        if (grade == 'A' or grade == 'a'):
            return '60', 'Grade A'
        elif (grade == 'B' or grade == 'b'):
            return '50', 'Grade B'
        elif (grade == 'C' or grade == 'c'):
            return '40', 'Grade C'
        elif (grade == 'D' or grade == 'd'):
            return '20', 'Grade D'

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
        password = "Iamjusttrying@10"
        message = EmailMessage()
        contain = "Student Info : \n" + "Student IUKL ID : " + str(
            self.IUKL_Code) + "\n" + "Student Name : " + self.Own_Name + "\n" + "Student Phone Number : " + str(
            self.Student_Phone_Number) + "\n" + "Student Gender : " + self.Student_Gender + "\n" + "Student Email : " \
                  + self.Student_Email + "\n" + "Student Grade : " + self.Student_Grade + "\n" + "Student Category : " \
                  + self.category + "\n" + "Student discount : " + self.discount
        message.set_content(contain)
        message['Subject'] = "Registration"
        message['From'] = "brcewayn01@gmail.com"
        message['To'] = "brcewayn01@gmail.com"
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("brcewayn01@gmail.com", password)
        server.send_message(message)
        server.quit()
        print("Email Sent")


if __name__ == '__main__':
    student = Student()
    student.Input_Student_Information()
    student.display_Student_Information()
    student.registrations()

