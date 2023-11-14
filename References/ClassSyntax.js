//#Create a class to model an object
class Example {
    constructor (param1, param2) {
        this.param1 = param1;
        this.param2 = param2;
    }

    myMethod (attr) {
        print("Code to Execute");
    }
}

//Create new instance of object class
myClassVar = new Example()

//Call methods of instance
myClassVar.myMethod()