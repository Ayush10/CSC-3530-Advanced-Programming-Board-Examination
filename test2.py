import smtplib
from email.message import EmailMessage


class MyCollege:
    def __init__(self):
        self.IUKLCode = 0
        self.CollegeName = ""
        self.TotalStudent = 0
        self.AreaOfCollege = 0
        self.DensityofCollege = 0

    def InputInformationOfCollege(self):
        print("Enter Data")
        self.IUKLCode = int(input("Enter IUKL ID : "))
        self.CollegeName = input("Enter College Name : ")
        self.TotalStudent = int(input("Enter Total Number of Student : "))
        self.AreaOfCollege = int(input("Enter Area of College : "))
        self.DensityofCollege = self.CalculateDensity()

    def CalculateDensity(self):
        return self.TotalStudent / self.AreaOfCollege

    def DensityInformation(self):
        print("==============")
        print("Info")
        print("==============")
        print("IUKL ID = " + str(self.IUKLCode))
        print("College Name = " + (self.CollegeName))
        print("Total Student = " + str((self.TotalStudent)))
        print("Area of College = " + str((self.AreaOfCollege)))
        print("Density of College = " + str((self.DensityofCollege)))

        if (self.TotalStudent > 1500 and self.TotalStudent < 5000):
            print("Highly Presence of Student")
            self.mailsend("admin1@iukl.com.np", "Highly Presence of Student")
        elif (self.TotalStudent >= 500 and self.TotalStudent <= 1500):
            print("average presence in the College")
            self.mailsend("admin2@iukl.com.np", "average presence in the College")
        elif (self.TotalStudent > 500):
            print("too less student in the college")
            self.mailsend("info@iukl.com.np", "too less student in the college")

    def mailsend(self, email, sub):
        password = "PASSWORD"
        msg = EmailMessage()
        contain = "Total Student = " + str(self.TotalStudent) + " CollegeName = " + str(
            self.CollegeName) + " IUKLCode = " + str(self.IUKLCode) + " Area of college = " + str(
            self.AreaOfCollege) + " Density of college = " + str(self.DensityofCollege)
        msg.set_content(contain)
        msg['Subject'] = sub
        msg['From'] = "brcewayn01@gmail.com"
        msg['To'] = email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("test@gmail.com", password)
        server.send_message(msg)
        server.quit()
        print("Email Send")

        # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # server.login("manishtmg099@gmail.com", "manish099")
        # server.sendmail("manishtmg099@gmail.com", self.email, self.presence)


test = MyCollege()
test.InputInformationOfCollege()
test.DensityInformation()