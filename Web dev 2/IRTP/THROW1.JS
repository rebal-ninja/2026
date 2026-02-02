let age = 19;
try {
    if (age < 18){
        throw "age must be above 18 to vote";
    }
    console.log("welcome to voting department");
} catch(error){
    console.log("errow",error)
    
}