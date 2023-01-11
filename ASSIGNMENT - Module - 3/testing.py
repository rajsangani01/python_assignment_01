import re

class banks :

    acno = 0
    acnm = ""
    actype = ""
    currbal = 0
    depobal = 0
    withbal = 0
    
    def create_ac(self) :
        self.acno = (input("Enter Ac No. :"))
        
        self.vacno = re.findall("[0-9]{11,11}",self.acno)
        if (self.vacno) :
            print("access :")
        else :
            print("not access :")
        
        self.acnm = (input("Enter Ac Name. :"))

        self.actype = (input("Enter Ac Type : Saving or Current :"))
        self.vactype = re.findall("[a-z]",self.actype)
        if self.vactype :
            print("access :")
        else :
            print("not access :")
        
        self.currbal = int(input("Enter Ac Current Balance :"))
        if self.currbal > 100000 :
            print("you fucker :")
        else :
            print("good man :")
        
        
        self.depobal = int(input("Enter Money You Want To Deposite : :"))
        if self.depobal > 10000 :
            print("not good :")
        else :
            print("good :")
        
        self.withbal = int(input("Enter Money You Want To Withdraw :"))
        if self.withbal > 1000 :
            print("not good :")
        else :
            print("good :")

bk = banks ()
bk.create_ac()


