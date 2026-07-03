// class car{
//     constructor(){
//         console.log("welcome to the showroom!")
//     }
//     display(model,year){
//         // let model = "m5";
//         // let year = 2012;
//         console.log("this is my car model "+model+" and year "+year)
//     }
// }
// let my_car = new car();
// let your_car = new car()


// my_car.display("zen",1998)
// your_car.display("skoda",2012)


// class car{
// constructor(model,year){
//     this.model = model
//     this.year = year
//     console.log("my car company")
//     // console.log("my car year",year)
// }
// display(){
//     console.log ("my car model is ",this.model)
//     console.log("my car year",this.year)
// }
// }
// let mycar = new car("skoda octavia",2012)
// mycar.display()


class details{
    constructor(name,dept,roll_no){
        this.name = name;
        this.dept = dept ;
        this.roll_no = roll_no;

        // console.log("The name of the student is"+name+"the department is"+dept+"the roll no "+roll_no)
        console.log("student details")
    }
        display (){1
            console.log("name of the student is ",this.name)
            console.log("department of the student is ",this.dept)
            console.log("roll no of the student is ",this.roll_no)
    }
}
let student = new details("Tez","cse",351);
student.display()