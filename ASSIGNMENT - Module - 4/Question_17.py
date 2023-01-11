# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle


class rectangle :

    length=0
    width=0

    def answer(self) :
        self.length=int(input('enter length of rectangle :'))
        self.width=int(input('enter width of rectangle :'))

    def printanswer(self) :
        print('area of rectangle :' ,self.length*self.width)

re = rectangle()
re.answer()
re.printanswer()