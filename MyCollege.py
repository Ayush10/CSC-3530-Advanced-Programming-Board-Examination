import smtplib
from email.message import EmailMessage


class MyCollege:
    def __init__(self, IUKL_code = 0, college_name = "", total_student = 0,
                 area_of_college = 0, density_of_college = 0):
        self.IUKLCode = IUKL_code
        self.CollegeName = college_name
        self.TotalStudent = total_student
        self.AreaOfCollege = area_of_college
        self.DensityOfCollege = density_of_college


    def CalculateDensity(self):
        density = self.TotalStudent / self.AreaOfCollege

        return density


    def InputInformationOfCollege(self):
        self.IUKLCode = int(input("Enter IUKL Code: "))
        self.CollegeName = input("Enter College Name: ")
        self.TotalStudent = int(input("Enter Total Number Of Student: "))
        self.AreaOfCollege = int(input("Enter Area Of College: "))
        self.DensityOfCollege = self.CalculateDensity()


    def DensityInformation(self):
        print("==============")
        print("Information")
        print("==============")
        print("IUKL ID = " + str(self.IUKLCode))
        print("College Name = " + (self.CollegeName))
        print("Total Student = " + str((self.TotalStudent)))
        print("Area of College = " + str((self.AreaOfCollege)))
        print("Density of College = " + str((self.DensityOfCollege)))
        if self.TotalStudent > 1500 < 5000:
            print("High Presence of Student")
            self.mailsend("admin1@iukl.com.np", "Highly Presence of Student")
        elif self.TotalStudent >= 500 <= 1500:
            print("Average Presence in the College")
            self.mailsend("admin2@iukl.com.np", "average presence in the College")
        elif self.TotalStudent < 500:
            print("too less student in the college")
            self.mailsend("info@iukl.com.np", "too less student in the college")

    def mailsend(self, email, subject):
        password = "Iamjusttrying@10"
        message = EmailMessage()
        contain = "Total Student = " + str(self.TotalStudent) + " CollegeName = " + str(
            self.CollegeName) + " IUKLCode = " + str(self.IUKLCode) + " Area of college = " + str(
            self.AreaOfCollege) + " Density of college = " + str(self.DensityOfCollege)
        message.set_content(contain)
        message['Subject'] = subject
        message['From'] = "brcewayn01@gmail.com"
        message['To'] = email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("brcewayn01@gmail.com", password)
        server.send_message(message)
        server.quit()
        print("Email Sent")



if __name__ == '__main__':
    college = MyCollege()
    college.InputInformationOfCollege()
    college.DensityInformation()


