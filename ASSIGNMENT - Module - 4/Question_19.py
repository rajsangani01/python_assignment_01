# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# types of different types of inheritance :

# 1. single inher.
# 2. mutiple inher.
# 3. multilevel inher.

# single inher :

'''class usersignup: #super
    fnm="Sanket"
    lnm="Chauhan"
    unm="sanket2020"
    pas="tops?123"
    def createuser(self):
        print("Firstname:",self.fnm)
        print("Lastname:",self.lnm)
        print("Username:",self.unm)
        print("Password:",self.pas)


class userlogin(usersignup): #sub
    def usersignin(self):
        print("Username:",self.unm)
        print("Password:",self.pas)


userlog=userlogin()
userlog.createuser()
userlog.usersignin()

# mutilevel inher :

class grandfather :
    land = 0
    gold = 0
    def g_data(self) :
        self.land = input("enter land :")
        self.gold = input("enter gold :")

class father(grandfather) :
    home = 0
    car = 0
    def f_data(self) :
        self.home = input("enter home :")
        self.car = input("enter car :")

class son(father) :
    stocks = 0
    bike = 0
    def s_data(self) :
        self.stocks = input("enter stocks :")    
        self.bike = input("enter bikes :")

    def allprop(self) :
        print("son land" ,self.land)


gf = son()
gf.g_data()
gf.f_data()
gf.s_data()
gf.allprop()'''

# multiple inher :

class raj :
    rid = 0
    rsub = ""
    def r_data(self) :
        self.rid = input("enter raj id :")
        self.rsub = input("enter raj sub :")

class rajesh :
    rjid = 0
    rjsub = ""
    def rj_data(self) :
        self.rjid = input("enter rajesh id :")
        self.rjsub = input("enter rajesh sub :")

class neel :
    nid = 0
    nsub = ""
    def n_data(self) :
        self.nid = input("enter neel id :")
        self.nsub = ("enter neel sub :")

class funcamp(raj,rajesh,neel) :
    def funcamp_data(self) :
        print("raj id :",self.rid)
        print("raj sub :",self.rsub)
        print("=====raj data========")
        print("rajesh id :",self.rjid)
        print("rajesh id :",self.rjsub)
        print("=====rajesh data=======")
        print("neel id :",self.nid)
        print("neel id :",self.nsub)
        print("=======neel data=======")
        
fn = funcamp()
fn.r_data()
fn.rj_data()
fn.n_data()
fn.funcamp_data()