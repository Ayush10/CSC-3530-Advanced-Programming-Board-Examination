import smtplib

class mycollege:
    def __init__(self, code = 0, cname = '', tstu = 0, area = 0, density = 0, presence = 0, email = ''):

        self.code = code
        self.cname = cname
        self.tstu = tstu
        self.area = area
        self.density = density
        self.presence = presence
        self.email = email


    def CalculateDensity(self):
        self.density = self.tstu/self.area


    def InputInformation(self):
        self.code = int(input("IUKL Code: "))
        self.cname = input("College Name: ")
        self.tstu = int(input("TOTAL Student: "))
        self.area = int(input("Area of College: "))
        self.density = int(input("Density of College: "))
        self.CalculateDensity()
        self.DensityInformation()


    def DensityInformation(self):
        print("-------------------------------------------------------------------")
        print(f'''
                IUKL Code: {self.code}
                College Name: {self.cname}
                Total Student: {self.tstu}
                Area of College: {self.area}
                Density of College: {self.density}
        ''')
        if(self.tstu > 1500 and self.tstu < 5000):
            self.presence = "Highly Presence of Student"
            self.email = "admin1@iukl.com.np"
            self.mail()
            print("Mail Sent")

        elif(self.tstu > 500 and self.tstu <= 1500):
            self.presence = "Average Presence in the college"
            self.email = "admin2@iukl.com.np"
            self.mail()
            print("Mail Sent")

        elif(self.tstu < 500):
            self.presence = "Too less student presence in the college"
            self.email = "info@iukl.com.np"
            self.mail()
            print("Mail Sent")

    def mail(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("tejendra.gurung1997@gmail.com", "tejendra")
        server.sendmail("tejendra.gurung1997@gmail.com", self.email, self.presence)



def main():
    college = mycollege()
    college.InputInformation()

main()