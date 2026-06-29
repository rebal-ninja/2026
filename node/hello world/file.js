const fs = require("fs")

// fs.writeFileSync("./test.txt", "hey there");
// THIS CREATES A FILE IN A SYNCHORNOUS MANNER 


// fs.writeFile("./test.txt","hello world async",(err)=> err)
// THIS CREATES A FILE IN AN ASYC MANNER 

// const result = fs.readFileSync("./contact.txt","utf-8");
// console.log(result)
// READS FILES IN SYN MANNER 

fs.readFile("./contact.txt","utf-8",(err,result)=>{
    if (err){
        console.log("error",err)
    }else{
        console.log(result )
    }
})
// ASYNCE READ CAN PUT THE RESULT INTO A VARIBLE 

 