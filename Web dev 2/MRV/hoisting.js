// let name = "abc ";
// let hto = 1234;
// let branch = "cse";

// function student()
// {
//     console.log("my name is ",name,"my roll no is ",hto,"my branch is ",branch);
// }
// student();


// USING PARAMETERIZED FUNCTION

// function student(name, hto, branch)
// {
//     console.log("my name is ",name,"my roll no is ",hto,"my branch is ",branch);
// }

// student("tez",1234,"cse");



// TAKING INPUTS WHILE ITS PARAMETRIZED FUNCTION


// let name = "abc ";
// let hto = 1234;
// let branch = "cse";

// function student(name,hto,branch)
// {
//     this.name = name;
//     this.hto = hto;
//     this.branch = branch;
//     console.log("my name is ",name,"my roll no is ",hto,"my branch is ",branch);
// }
// student();


// THIS KEYWORD

function student(name,htno){
console.log("my name is " + name + ", my halltno is " + htno);
}

const person = {name:"abc",htno:234};
student.call(person,person.name,person.htno);