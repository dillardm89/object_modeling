#Create a class to model an object
class Example:
    def _init_ (self, param1):
        self.param1 = param1

    def _str_(self):
        return f"This is a return statement when class is called in print statement."

    def myfunc(self):
        print("Code to Execute")


#Create new instance of object class
myClassVar = Example()

#Call methods of instance
myClassVar.myfunc()

#Print return string for instance
print(myClassVar)